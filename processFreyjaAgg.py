#!/usr/bin/env python

#	summarized	lineages	abundances	resid	coverage
#BBW-0319_S1_trimmed.variants.tsv	[('BQ.1* [Omicron (BQ.1.X)]', 0.7680493077157702), ('Omicron', 0.11280316860125204), ('BA.2.75* [Omicron (BA.2.75.X)]', 0.0452871256925549), ('BA.5* [Omicron (BA.5.X)]', 0.025235970787643253)]	BQ.1.12 BQ.1.27 BQ.1.2 BQ.1.1.8 BQ.1.1 XBB.1 BA.2.3.2 BQ.1.19 CW.1 BA.2.75.6 XBB.1.5 BA.5.2.34 BA.5.2.16 BQ.1.1.15 BQ.1.26 CP.4 BA.2.75.10 BQ.1.1.3 BA.2.3.4 BQ.1.1.10 BQ.1.17 BA.2.3.7 BQ.1.1.26 BQ.1.25 BA.2.75.8 BQ.1.1.1 BM.6 BQ.1.1.11 BQ.1.1.21 BA.5.2.13 BA.2.8 CA.6 BQ.1.18 CN.2 BA.2.82 BF.19 BQ.1.1.18 CC.1 BA.2.5 BQ.1.1.24 BA.5.2.33 BZ.1 BA.5.2.39 XBG XBB.2	0.35375300 0.08578592 0.08022440 0.07043772 0.07043772 0.05248758 0.04136915 0.03836077 0.03814482 0.03722247 0.00810630 0.00698658 0.00631589 0.00601914 0.00418499 0.00298770 0.00283286 0.00260870 0.00243061 0.00241752 0.00237565 0.00210970 0.00210342 0.00210084 0.00197889 0.00190396 0.00174986 0.00170177 0.00161160 0.00160772 0.00159642 0.00150305 0.00148976 0.00148399 0.00145974 0.00140873 0.00126904 0.00122612 0.00116800 0.00111857 0.00110011 0.00106383 0.00105530 0.00104822 0.00102746	8.415629236026737	91.70317359462261

import sys

sample_dict={}

with open(sys.argv[1]) as infile:
    next(infile)
    for line in infile:
        tmpline=line.strip().split('\t')
        sample=tmpline[0]
        lineages=tmpline[2].split(' ')
        abundances=tmpline[3].split(' ')
        sample_dict[sample]={}
        for idx,lineage in enumerate(lineages):
            sample_dict[sample][lineage]=abundances[idx]

with open(sys.argv[2],'w') as outfile:
    keyset=set()
    for sampledata in sample_dict.values():
        for lineage_key in sampledata.keys():
            keyset.add(lineage_key)
    keylist=list(keyset)
    print(keylist)
    outfile.write('\t'.join(['Sample']+keylist)+'\n')

    for sample,sampledata in sample_dict.items():
        outline=[sample]
        for lineage_key in keylist:
            try:
                outline.append(sampledata[lineage_key])
            except KeyError:
                outline.append('NA')
        outfile.write('\t'.join(outline)+'\n')
