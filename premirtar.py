import argparse
from argparse import ArgumentParser
import os
import pathlib
import pandas as pd

parser = ArgumentParser(description='PreMirTar\nPlease type in the full path of miRNA and transcriptome data for analyzing!')
parser.add_argument("miRNA", help="Full path of the microRNA fasta file.")
parser.add_argument("transcritome", help="Full path of the transcriptome fasta file.")

args = parser.parse_args()

with open(args.miRNA) as file, open(args.transcritome) as file:

    print("Full path to miRNA fasta file:", args.miRNA)
    print("Full path to transcriptome fasta file:", args.transcritome)
    print("===============================================\nBuilding BOWTIE database...")
    os.system("bowtie-build -q %s bowtie" %(args.transcritome))
    print("===============================================\nAnalyzing with BOWTIE...")
    os.system("bowtie -p 24 -a -f -l 5 -n 3 -e 360 -k 9999999 --fullref --norc --best bowtie %s > miRNA.bowtied" %(args.miRNA))
    print("===============================================\nCalculating by mirScore...")
    os.system("rm *.ebwt")
    os.system("%s/mirScore.rb/mirScore.script miRNA.bowtied" %(pathlib.Path().absolute()))
    print("===============================================\nConverting to MirTarSite files...")
    df = pd.read_csv("%s/miRNA.bowtied.target.predict.tsv" %(pathlib.Path().absolute()), sep="\t")
    pd.set_option('display.max_rows', None)
    all_mir = r"%s/output/all_mir.csv" %(pathlib.Path().absolute())
    df.to_csv("%s/site_name.csv" %(pathlib.Path().absolute()), sep = "\t", index = False, header = False, columns=["Contig_Name"])
    df.to_csv("%s/targetsite.csv" %(pathlib.Path().absolute()), sep = "\t", index = False, header = False, columns=["Target_site"])
    df.to_csv("%s/tagsequence.csv" %(pathlib.Path().absolute()), sep = "\t", index = False, header = False, columns=["Tag_sequence"])
    df.to_csv(all_mir, line_terminator = "\n>" , sep = "\n", index = False , header = False , columns=["Tag_ID", "Tag_sequence"] )
    df.to_csv("%s/strand.csv" %(pathlib.Path().absolute()), sep = "\t", index = False, header = False, columns=["Strand"])
    df["Contig_Name"] = df["Contig_Name"].str.replace(' ', '-')
    df.to_csv("%s/output/interaction_pair.txt" %(pathlib.Path().absolute()), sep = "\t", index = False , header = False , columns=["Tag_ID" , "Contig_Name"])
    frStr = open("%s/strand.csv" %(pathlib.Path().absolute()), "r")
    frLst = open("%s/site_name.csv" %(pathlib.Path().absolute()), "r")
    frSeq = open("%s" %(args.transcritome), "r")
    frSta = open("%s/targetsite.csv" %(pathlib.Path().absolute()), "r")
    frEnd = open("%s/tagsequence.csv" %(pathlib.Path().absolute()), "r" )
    fwOut = open("%s/output/all_site.fa" %(pathlib.Path().absolute()), "w")
    query = []
    database = {}
    trans = {ord('A'): 'T', ord('T'): 'A', ord('G'): 'C', ord('C'): 'G'}
    for i in frLst.readlines():
        query.append(i.strip())
    for i in frSeq.readlines():
        if i.startswith(">"):
            keys = i.lstrip(">").strip()
            database[keys] = []
        else:
            database[keys].append(i.strip())
    for line in query:
        strand = frStr.readline()
        sta = frSta.readline()
        sta = int(sta)
        end = frEnd.readline()
        end = int(len(end))
        end += sta - 1
        fwOut.write(">" + str(line).replace(" ","-") + "\n" + str("".join(database[line])[sta:end][::-1]).translate(trans) + "\n")
    fwOut.close()

    with open(all_mir, "r") as f:
        first = f.readline().strip()
    with open(all_mir, "r") as d:
        list_of_lines = d.readlines()
        list_of_lines[0] = ">%s\n" %(first)
    with open(all_mir, "w") as d:
        d.writelines(list_of_lines)
    with open(all_mir,"r") as fd:
        d=fd.read()
        m=d.split("\n")
        s="\n".join(m[:-1])
    with open(all_mir,"w+") as fd:
        for i in range(len(s)):
            fd.write(s[i])
    os.system("mv ./miRNA.bowtied.target.predict.tsv ./output/miRNA_target_score.txt")
    os.system("rm *.csv")
    os.system("rm miRNA.bowtied")
    print("All the result files are in %s/output" %(pathlib.Path().absolute()))

    print("===============================================\nAnalyzing with MirTarSite...")
    if __name__=='__main__':
        os.system("python3 %s/mirtarsite/custom_predict.py %s/mirtarsite/state_dict/b16_lr0.001_embd100_rnnlayer1_rnnhidden100_drop0.3_ep47.pth %s/output/all_mir.fa %s/output/all_site.fa %s/output/interaction_pair.txt %s/mirtarsite/example/output_result.txt --cuda True" %(pathlib.Path().absolute(), pathlib.Path().absolute(), pathlib.Path().absolute(), pathlib.Path().absolute(), pathlib.Path().absolute(), pathlib.Path().absolute()))
    df = pd.read_csv("%s/mirtarsite/example/output_result.txt" %(pathlib.Path().absolute()), sep="\t")
    df.columns = ["microRNA", "target", "prediction"]
    pd.set_option('display.max_rows', None)
    with open("%s/output/mirRTarget_result_success.txt" %(pathlib.Path().absolute()), "w") as fd1, open("%s/output/miRTarget_result_false.txt" %(pathlib.Path().absolute()), "w") as fd2:
        print(df[df["prediction"] == 1], file = fd1)
        print(df[df["prediction"] == 0], file = fd2)
    print("Successfully analyze with miRTarget!\nYou can find your result at :%s/output/" %(pathlib.Path().absolute()))