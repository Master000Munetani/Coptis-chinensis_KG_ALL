from django.shortcuts import render, HttpResponse
import os
import time
import json
import csv
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .qatools import *
from .pyneo_utils import *
from django.views.decorators.csrf import csrf_exempt
import jieba
from .models import MyNode
from django.conf import settings
# Create your views here.

def index(request):
    try:
        pass
    except Exception as e:
        print(e)
    return render(request, "index.html", locals())

def search(request):
    try:
        start = request.GET.get("start", "")
        relation = request.GET.get("relation", "")
        end = request.GET.get("end", "")
        all_datas = get_all_relation(start, relation, end)
        links = json.dumps(all_datas["links"])
        datas = json.dumps(all_datas["datas"])
        categories = json.dumps(all_datas["categories"])
        legend_data = json.dumps(all_datas["legend_data"])

        print(categories)
        print(legend_data)
    except Exception as e:
        print(e)
    return render(request, "search.html", locals())

def wenda(request):
    data_set= ['基因', '化合物', '疾病', '古籍方剂', 'GOterm', '通路', '中成药', '中医学症状', '现代医学症状', '证候', '药物', '症状发生位置']
    weather_guanxi = []
    try:

        if request.method == "GET":
            key = request.GET.get("key", "")
            question = key

            if key:
                daan = ""
                cibiao_path = os.path.join(settings.DATAS_DIR, "cibiao.txt")
                print(cibiao_path)
                jieba.load_userdict(cibiao_path)

                qiecis = jieba.cut(key)
                # print(qiecis)
                shibie = {}
                qiecishibie = []
                for qieci in qiecis:
                    # print(qieci)
                    # if qieci in STOP_WORDS:
                    #     continue
                    qiecishibie.append(qieci)
                    print("==ori==")
                    print(qieci)
                    nodes = MyNode.objects.filter(name=qieci)
                    print("====")
                    print(nodes)
                    if len(nodes) == 0:
                        if qieci in data_set:
                            shibie["type"] = qieci
                            continue
                        elif str(qieci) =="relationship":
                            weather_guanxi.append(qieci)
                            continue
                        else:
                            continue

                    last_node = nodes[0]
                    for node in nodes:
                        if node.leixing == "GovNode":
                            last_node = node

                    print(last_node)
                    print(last_node.name)

                    if "relation" in shibie.keys() and len(last_node.name) > 1:
                        shibie[last_node.leixing] = last_node.name
                    elif "relation" not in shibie.keys():
                        shibie[last_node.leixing] = last_node.name
                    else:
                        pass
                    # shibie[last_node.leixing] = last_node.name
                    print(shibie)
                    # print(weather_guanxi)
                print(shibie)
                g = Graph('http://localhost:7474', user='neo4j', password='yslin20021206L')
                daan = ""
                if len(shibie.keys()) == 2 and "guanxi" in shibie and len(weather_guanxi) == 0:
                    # APEX1的相关疾病有哪些
                    need_key = ""
                    need_value = ""
                    for mykey in shibie.keys():
                        if mykey != "guanxi":
                            need_key = mykey # 中药
                            need_value = shibie[mykey] # 黄连

                    print("命中模板2hr")
                    sql = "MATCH (n)-[r:`%s`]->(b) where n.name='%s' RETURN n,b" % (shibie["guanxi"], need_value)
                    print(sql)
                    nodes_data_all = g.run(sql).data()
                    if len(nodes_data_all) == 0:
                        sql = "MATCH (n)<-[r:`%s`]-(b) where b.name='%s' RETURN b" % (shibie["guanxi"], need_value)
                        print(sql)
                        nodes_data_all = g.run(sql).data()

                    mnjh = ""
                    img = ""
                    for nodes_relations in nodes_data_all:
                        print(nodes_relations['b'])
                        node_dict = dict(nodes_relations['b'])
                        nnode_dict = dict(nodes_relations['n'])
                        print("查找到节点:" + str(node_dict))

                        mnjh = mnjh + node_dict["name"] + "；"

                    daan = "%s%s:\t%s" % (need_value, shibie["guanxi"], mnjh)
                elif len(shibie.keys()) == 3 and "guanxi" in shibie and len(weather_guanxi) == 0:
                    # 黄连与哪些疾病存在潜在联系
                    print("命中模板1hrt")
                    pipei = []
                    for mkey in shibie.keys():
                        if mkey != "guanxi" and mkey != "relation":
                            pipei.append(shibie[mkey])
                    sql = "MATCH (n)-[r:%s]->(b) where n.name='%s' and b:%s RETURN b" % (shibie["guanxi"], pipei[0], pipei[1])
                    print(sql)
                    nodes_data_all = g.run(sql).data()
                    mnjh = ""
                    for nodes_relations in nodes_data_all:
                        print(nodes_relations['b'])
                        node_dict = dict(nodes_relations['b'])
                        print("查找到节点:" + str(node_dict))

                        mnjh = mnjh + node_dict["name"] + "；"

                    daan = "与%s存在%s的有：\t%s" % (pipei[0], shibie["guanxi"], mnjh)
                elif "guanxi" not in shibie and len(shibie.keys()) == 2 and len(weather_guanxi) !=0:
                    # KITLG与Anemia之间的relationship是什么
                    print("命中模板guanxi")
                    pipei = []
                    for key in shibie.keys():
                        pipei.append(shibie[key])
                    print(pipei)
                    sql = "MATCH (n)-[r]-(b) where b.name='%s' and n.name='%s' RETURN r" % (pipei[1],pipei[0])
                    print(sql)
                    nodes_data_all = g.run(sql).data()
                    # p=pipei[0]
                    mnjh = ""
                    for nodes_relations in nodes_data_all:
                        print(nodes_relations['r'])
                        # node_dict = dict(nodes_relations['r']) str(nodes_relations['r'].keys).split(" ")[4]
                        print("查找到关系:" + str(nodes_relations['r'].keys).split(" ")[4])
                        mnjh = mnjh + str(nodes_relations['r'].keys).split(" ")[4] + "；"
                        # if "img" in node_dict:
                        #     img = node_dict["img"]

                    daan = "%s和%s之间存在的关系:\t%s" % (pipei[0],pipei[1], mnjh)
                elif "guanxi" not in shibie and len(shibie.keys()) == 2 and len(weather_guanxi) == 0:
                    # 黄连与哪些疾病有关
                    print("命中模板3ht")
                    pipei = []
                    for key in shibie.keys():
                        pipei.append(shibie[key])
                    print(pipei)
                    sql = "MATCH (n)-[r]->(b) where b:%s and n.name='%s' RETURN b" % (pipei[1],pipei[0])
                    print(sql)
                    nodes_data_all = g.run(sql).data()
                    # p=pipei[0]
                    if len(nodes_data_all) == 0:
                        sql = "MATCH (n)<-[r]-(b) where b:%s and n.name='%s' RETURN b" % (pipei[1],pipei[0])
                        print(sql)
                        nodes_data_all = g.run(sql).data()
                    mnjh = ""
                    for nodes_relations in nodes_data_all:
                        print(nodes_relations['b'])
                        node_dict = dict(nodes_relations['b'])
                        print("查找到节点:" + str(node_dict))
                        mnjh = mnjh + node_dict["name"] + "；"
                        if "img" in node_dict:
                            img = node_dict["img"]

                    daan = "%s的相关%s:\t%s" % (pipei[0],pipei[1], mnjh)

                else:
                    daan = "暂时不支持此类问题，可以试试问：黄连的相关基因有什么？"


                print("====")
                print(qiecishibie)
                print(shibie)
            return render(request, "wenda.html", locals())
    except Exception as e:
        print(e)
        return render(request, "wenda.html", locals())


def init_ci(request):
    cibiao_path = os.path.join(settings.DATAS_DIR, "cibiao.txt")

    ci_list = []
    for data in MyNode.objects.filter():
        if data.name not in ci_list:
            ci = open(cibiao_path, "a", encoding="utf-8-sig")
            ci.write(data.name + "\n")
            ci.close()
            ci_list.append(data)

    return HttpResponse("ok")


def init_node_datas(request):
    g = Graph('http://localhost:7474', user='neo4j', password='yslin20021206L')
    cibiao_path = os.path.join(settings.DATAS_DIR, "cibiao.txt")
    ci = open(cibiao_path, "a", encoding="utf-8")
    ci_list = []
    lable_list = []

    sql = "MATCH (n) RETURN n"
    g = Graph('http://localhost:7474', user='neo4j', password='yslin20021206L')

    nodes_data_all = g.run(sql).data()
    for nodes_relations in nodes_data_all:
        try:
            print(nodes_relations)
            print(nodes_relations['n'])
            print(nodes_relations['n'].labels)
            print(dir(nodes_relations['n']))
            print(dict(nodes_relations['n'])['name'])

            name = dict(nodes_relations['n'])['name']
            lable = str(nodes_relations['n'].labels)
            if need_clean_str(dict(nodes_relations['n'])['name']):
                name = clean_str(dict(nodes_relations['n'])['name'])
                nodes_relations['n']["name"] = name
                g.push(nodes_relations['n'])
            if need_clean_str(str(nodes_relations['n'].labels)):
                lable = clean_str(str(nodes_relations['n'].labels))

            if name not in ci_list:
                ci.write(name + "\n")
                ci_list.append(name)

            if lable not in ci_list:
                ci.write(lable + "\n")
                ci_list.append(lable)

            if lable not in lable_list:
                lable_list.append(lable)

            nameobj = MyNode.objects.filter(name=name, leixing=lable)
            if len(nameobj) == 0:
                nameobj = MyNode()
            else:
                nameobj = nameobj[0]
            nameobj.name = name
            nameobj.leixing = lable
            nameobj.save()

            node_dict = dict(nodes_relations['n'])

            for attr in node_dict.keys():
                if attr == "name":
                    continue
                attr_name = attr
                attr_value = node_dict[attr_name]

                if need_clean_str(node_dict[attr]):
                    attr_value = clean_str(node_dict[attr])

                    nodes_relations['n'][attr_name] = attr_value
                    g.push(nodes_relations['n'])

                if attr_value not in ci_list:
                    ci.write(attr_value + "\n")
                    ci_list.append(attr_value)

                    attrobj = MyNode.objects.filter(name=attr_value, leixing=attr_name)
                    if len(attrobj) == 0:
                        attrobj = MyNode()
                    else:
                        attrobj = attrobj[0]
                    attrobj.name = attr_value
                    attrobj.leixing = attr_name
                    attrobj.save()

        except Exception as e:
            print(e)
            continue
    ci.close()
    return HttpResponse("ok")


def clean_str(need_str):
    if need_clean_str(need_str):
        last_str = need_str.replace("、", "").replace(":", "").replace("，", "")
    else:
        last_str = need_str
    return last_str


def need_clean_str(need_str):
    if "、" in need_str or ":" in need_str or "，" in need_str:
        return True
    else:
        return False


def init_relation_datas(request):
    # g = Graph('http://localhost:7474', user='neo4j', password='123456')
    cibiao_path = os.path.join(settings.DATAS_DIR, "cibiao.txt")
    ci = open(cibiao_path, "a", encoding="utf-8")
    ci_list = []

    # sql = "MATCH p=()-->() RETURN p"
    # g = Graph('http://localhost:7474', user='neo4j', password='123456')

    # nodes_data_all = g.run(sql).data()
    relation = data = ['关系', '协变', '属于', '来源典籍', '治疗', '潜在联系', '症状发生位置', '相互作用', '相关GOterm', '相关中医学症状', '相关中成药', '相关化合物', '相关古籍方剂', '相关基因', '相关现代医学症状', '相关疾病', '相关证候', '相关通路', '起调控作用']

    for nodes_relations in relation:
        try:
            print("===")
            rel = clean_str(nodes_relations)
            if rel not in ci_list:
                ci.write(rel + "\n")
                ci_list.append(rel)

            relobj = MyNode.objects.filter(name=rel, leixing="guanxi")
            if len(relobj) == 0:
                relobj = MyNode()
            else:
                relobj = relobj[0]
            relobj.name = rel
            relobj.leixing = "guanxi"
            relobj.save()
        except Exception as e:
            print(e)
            continue

    ci.close()
    return HttpResponse("ok")