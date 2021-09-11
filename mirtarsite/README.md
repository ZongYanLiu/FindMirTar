# MirTarSite
end-to-end microRNA target mrna site prediction

A tool for predicting microRNA target site, given a pair of microRNA and mRNA target sites predict if it's a functional effective miRNA:mRNA interaction.

## Predict custom data

### Requirements
#### Dependencies
* Python 3.7+
* argparse
* torch
* numpy

#### Input 
* microRNA fasta file
```
>hsa-miR-183-5p
UAUGGCACUGGUAGAAUUCACU
>hsa-miR-33a-5p
GUGCAUUGUAGUUGCAUUGCA
...
...
```
* mRNA target site fasta file
```
>AANAT_site_0
TTACCGTGCTGATTACTGTGCTA
>ABCA1_site_9
AACGTAACTTAACGTAACGTAACTTATCATAGTCATGT
...
...
```
* interaction pair file
```
hsa-miR-183-5p  AANAT_site_0    
hsa-miR-33a-5p  ABCA1_site_9    
hsa-miR-129-5p  ABCB1_site_1    
hsa-miR-451a    ABCB1_site_2 
hsa-miR-129-5p  ABCB1_site_4
...
...
```
* pretrain state dict file

#### Usage
```
usage: custom_predict.py [-h] [--batch_size BATCH_SIZE]
                         [--model_type MODEL_TYPE]
                         [--embedding_hidden EMBEDDING_HIDDEN]
                         [--rnn_hidden RNN_HIDDEN] [--rnn_layer RNN_LAYER]
                         [--class_dropout CLASS_DROPOUT]
                         [--threshold THRESHOLD]
                         state_dict_file miRNA_file site_file interaction_pair
                         output_file

mirtarsite
end-to-end microRNA target mrna site prediction tool

Input: microRNA,mRNA target site fasta file,pretrained state dict file
(Default hyperparameter seeting is the same as my pretrained state dict file)

positional arguments:
  state_dict_file       state dict for model
  miRNA_file            microRNA fasta file 5'->3' sequence
  site_file             mRNA target site fasta file 3'->5' sequence
  interaction_pair      interaction pairs for the given microRNA and mRNA
                        target site fasta file
  output_file           output predction file

optional arguments:
  -h, --help            show this help message and exit
  --batch_size BATCH_SIZE
  --model_type MODEL_TYPE
  --embedding_hidden EMBEDDING_HIDDEN
                        size of hidden in embedding
  --rnn_hidden RNN_HIDDEN
                        size of hidden in RNN layer
  --rnn_layer RNN_LAYER
                        num of layer for RNN
  --class_dropout CLASS_DROPOUT
                        dropout in classify layer
  --threshold THRESHOLD
                        threshold for binary classification

```

#### example command
```
# state dict for V2 dataset (recommend)
python3 custom_predict.py ./state_dict/b16_lr0.001_embd100_rnnlayer1_rnnhidden100_drop0.3_ep47.pth ./example/all_mir.fa ./example/all_site.fa ./example/interaction_pair.txt ./example/out_V2.txt --cuda True
# state dict for V1 dataset
python3 custom_predict.py ./state_dict/deepmirtar_b64_lr0.001_embd100_rnnlayer1_rnnhidden400_drop0_ep9.pth ./example/all_mir.fa ./example/all_site.fa ./example/interaction_pair.txt ./example/out_V1.txt --cuda True  --rnn_hidden 400 --class_dropout 0 --threshold 0.7
```
