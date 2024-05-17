# "C:\Users\15382\Desktop\process\ID/gene_entrezID.txt"
# my @array0=();
# open(IN,"C:/Users/15382/Desktop/process/ID/gene_entrezID.txt") || die "$!";
# while (<IN>) {
#     chomp($_);
#     if (!$_) {
#         next;
#     }
#     else  {
#         my @temp=split("\t",$_);
#         my $c =  "Gene::".$temp[1];
#        push(@array0,$c); 
#     }
# }
# my @array00 =("Hetionet::GcG::Gene:Gene","Hetionet::GiG::Gene:Gene","Hetionet::Gr>G::Gene:Gene");
# open(IN1,"C:/Users/15382/Desktop/drkg.txt") || die "$!";
# open(OUT,">C:/Users/15382/Desktop/drkg-gene.txt") || die "$!";
# while (<IN1>) {
#     chomp($_);
#     if(!$_){
#         next;
#     }
#     else {
#             my @temp1=split("\t",$_);
#             if (($temp1[1] eq "Hetionet::GpPW::Gene:Pathway") and grep { $_ eq $temp1[0] } @array0) {
#                print OUT $temp1[0]."\t".$temp1[1]."\t".$temp1[2]."\n";
#             }
#             elsif (grep { $_ eq $temp1[1] } @array00) {
#                 if (grep{$_ eq $temp1[0]}@array0 and grep{$_ eq $temp1[2]}@array0) {
#                    print OUT $temp1[0]."\t".$temp1[1]."\t".$temp1[2]."\n";
#                 }
#                 else  {
#                     next;
#                 }
#             }
#             else  {
#                 next;
#             }
            
#         }
# }
# close(IN1);
# close(OUT);

# my @array=();
# open(IN,"C:/Users/15382/Desktop/process/ID/gene_entrezID.txt") || die "$!";
# while (<IN>) {
#     chomp($_);
#     if (!$_) {
#         next;
#     }
#     else  {
#         my @temp=split("\t",$_);
#         my $c =  "Gene::".$temp[1];
#        push(@array,$c); 
#     }
# }
# close(IN);
# my @array0=();
# open(IN,"C:/Users/15382/Desktop/process/all_disease.txt") || die "$!";
# while (<IN>) {
#     chomp($_);
#     if (!$_) {
#         next;
#     }
#     else  {
#        push(@array0,$_); 
#     }
# }
# close(IN);
# my @array00 =("Hetionet::DdG::Disease:Gene","Hetionet::DuG::Disease:Gene","Hetionet::DaG::Disease:Gene");
# open(IN1,"C:/Users/15382/Desktop/drkg.txt") || die "$!";
# open(OUT,">C:/Users/15382/Desktop/drkg-disease.txt") || die "$!";
# while (<IN1>) {
#     chomp($_);
#     if(!$_){
#         next;
#     }
#     else {
#             my @temp1=split("\t",$_);
#             if (grep { $_ eq $temp1[1] } @array00) {
#                 if (grep{$_ eq $temp1[0]}@array0 and grep{$_ eq $temp1[2]}@array) {
#                    print OUT $temp1[0]."\t".$temp1[1]."\t".$temp1[2]."\n";
#                 }
#                 else  {
#                     next;
#                 }
#             }
#             else  {
#                 next;
#             }
            
#         }
# }
# close(IN1);
# close(OUT);

my @array1=();
open(IN,"C:/Users/15382/Desktop/process/all_compound.txt") || die "$!";
while (<IN>) {
    chomp($_);
    if (!$_) {
        next;
    }
    else  {
       push(@array1,$_); 
    }
}
close(IN);
my @array=();
open(IN,"C:/Users/15382/Desktop/process/ID/gene_entrezID.txt") || die "$!";
while (<IN>) {
    chomp($_);
    if (!$_) {
        next;
    }
    else  {
        my @temp=split("\t",$_);
        my $c =  "Gene::".$temp[1];
       push(@array,$c); 
    }
}
close(IN);
my @array0=();
open(IN,"C:/Users/15382/Desktop/process/all_disease.txt") || die "$!";
while (<IN>) {
    chomp($_);
    if (!$_) {
        next;
    }
    else  {
       push(@array0,$_); 
    }
}
close(IN);
my @array00 =("DRUGBANK::target::Compound:Gene","DRUGBANK::enzyme::Compound:Gene","DRUGBANK::carrier::Compound:Gene"
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
            if (grep { $_ eq $temp1[1] } @array00) {
                if (grep{$_ eq $temp1[0]}@array1 and grep{$_ eq $temp1[2]}@array) {
                   print OUT $temp1[0]."\t".$temp1[1]."\t".$temp1[2]."\n";
                }
                elsif(grep{$_ eq $temp1[2]}@array0)  {
                   print OUT $temp1[0]."\t".$temp1[1]."\t".$temp1[2]."\n";
                }
                else  {
                    next;
                }
            }
            else  {
                next;
            }
            
        }
}
close(IN1);
close(OUT);