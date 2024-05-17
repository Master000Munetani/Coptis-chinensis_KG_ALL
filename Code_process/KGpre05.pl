# # GNBR::B::Gene:Gene
# # GNBR::W::Gene:Gene
# # GNBR::V+::Gene:Gene
# # GNBR::E+::Gene:Gene
# # GNBR::E::Gene:Gene
# # GNBR::I::Gene:Gene
# # GNBR::H::Gene:Gene
# # GNBR::Rg::Gene:Gene
# # GNBR::Q::Gene:Gene
# # Hetionet::GpPW::Gene:Pathway
# # Hetionet::GpCC::Gene:Cellular Component
# # Hetionet::GpMF::Gene:Molecular Function
# my @array0=();
# open(IN,"C:/Users/15382/Desktop/process/HuangLian-Gene.txt") || die "$!";
# while (<IN>) {
#     chomp($_);
#     if (!$_) {
#         next;
#     }
#     else  {
#         my @temp=split("\t",$_);
#        push(@array0,$temp[2]); 
#     }
# }

# my @array =("GNBR::B::Gene:Gene","GNBR::W::Gene:Gene","GNBR::V+::Gene:Gene","GNBR::E+::Gene:Gene"
# ,"GNBR::E::Gene:Gene","GNBR::I::Gene:Gene","GNBR::H::Gene:Gene","GNBR::Rg::Gene:Gene","GNBR::Q::Gene:Gene",
# "Hetionet::GpPW::Gene:Pathway","Hetionet::GpCC::Gene:Cellular Component","Hetionet::GpMF::Gene:Molecular Function","Hetionet::GpBP::Gene:Biological Process");
# open(IN1,"C:/Users/15382/Desktop/drkg.txt") || die "$!";
# open(OUT,">C:/Users/15382/Desktop/drkg-gene.txt") || die "$!";
# while (<IN1>) {
#     chomp($_);
#     if(!$_){
#         next;
#     }
#     else {
#             my @temp1=split("\t",$_);
#             if (grep { $_ eq $temp1[1] } @array) {
#                 if (grep{$_ eq $temp1[0]}@array0 or grep{$_ eq $temp1[2]}@array0) {
#                    print OUT $temp1[0]."\t".$temp1[1]."\t".$temp1[2]."\n";
#                 }
#             }
#             else  {
#                 next;
#             }
            
#         }
        
    
# }
# close(IN1);
# close(OUT);


# # Hetionet::DpS::Disease:Symptom
# # Hetionet::DdG::Disease:Gene
# # Hetionet::DuG::Disease:Gene
# my @array0=();
# open(IN,"C:/Users/15382/Desktop/process/HuangLian-Disease.txt") || die "$!";
# while (<IN>) {
#     chomp($_);
#     if (!$_) {
#         next;
#     }
#     else  {
#         my @temp=split("\t",$_);
#        push(@array0,$temp[2]); 
#     }
# }
# my @array =("Hetionet::DpS::Disease:Symptom","Hetionet::DdG::Disease:Gene","Hetionet::DuG::Disease:Gene");
# open(IN1,"C:/Users/15382/Desktop/drkg.txt") || die "$!";
# open(OUT,">C:/Users/15382/Desktop/drkg-disease.txt") || die "$!";
# while (<IN1>) {
#     chomp($_);
#     if(!$_){
#         next;
#     }
#     else {
#             my @temp1=split("\t",$_);
#             if (grep { $_ eq $temp1[1] } @array) {
#                 if (grep{$_ eq $temp1[0]}@array0 ) {
#                    print OUT $temp1[0]."\t".$temp1[1]."\t".$temp1[2]."\n";
#                 }
#             }
#             else  {
#                 next;
#             }
            
#         }
        
    
# }
# close(IN1);
# close(OUT);

# DRUGBANK::target::Compound:Gene ——>target::Compound:Gene
# DRUGBANK::enzyme::Compound:Gene
# DRUGBANK::carrier::Compound:Gene
# DRUGBANK::treats::Compound:Disease
my @array0=();
open(IN0,"C:/Users/15382/Desktop/process/HuangLian-Gene.txt") || die "$!";
while (<IN0>) {
    chomp($_);
    if (!$_) {
        next;
    }
    else  {
        my @temp=split("\t",$_);
       push(@array0,$temp[2]); 
    }
}
close(IN0);
my @array00=();
open(IN,"C:/Users/15382/Desktop/process/HuangLian-Disease.txt") || die "$!";
while (<IN>) {
    chomp($_);
    if (!$_) {
        next;
    }
    else  {
        my @temp=split("\t",$_);
       push(@array00,$temp[2]); 
    }
}
close(IN);
my @array =("DRUGBANK::target::Compound:Gene","DRUGBANK::enzyme::Compound:Gene","DRUGBANK::carrier::Compound:Gene"
,"DRUGBANK::treats::Compound:Disease");
open(IN1,"C:/Users/15382/Desktop/drkg.txt") || die "$!";
open(OUT,">C:/Users/15382/Desktop/drkg-compound.txt") || die "$!";
while (<IN1>) {
    chomp($_);
    if(!$_){
        next;
    }
    else {
            my @temp1=split("\t",$_);
            if (grep { $_ eq $temp1[1] } @array) {
                if ($temp1[1] eq "DRUGBANK::target::Compound:Gene" ) {
                    if (grep { $_ eq $temp1[2] } @array0 ) {
                        print OUT $temp1[0]."\t"."target::Compound:Gene"."\t".$temp1[2]."\n";
                    }
                    else  {
                        next;
                    }
                }
                else  {
                    if (grep { $_ eq $temp1[2] } @array0 or grep { $_ eq $temp1[2] } @array00) {
                        print OUT $temp1[0]."\t".$temp1[1]."\t".$temp1[2]."\n";
                    }
                    else  {
                        next;
                    }
                    
                }
                   
            }
            else  {
                next;
            }
            
        }
        
    
}
close(IN1);
close(OUT);


# my $a = 1;
# my $aa ="Gene".$a;
# my @aaa=();
# push(@aaa,$aa);
# print @aaa