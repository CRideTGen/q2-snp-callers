from pathlib import Path
from random import randint
from time import sleep

from q2_nasp2_types.alignment import BAMFileFormat, BAMFileDirFmt
from q2_nasp2_types.snp import VCFFileDirFmt
from q2_types.feature_data import DNAFASTAFormat


def haplotype_caller(sequences: BAMFileDirFmt, ref_genome: DNAFASTAFormat = None) -> VCFFileDirFmt:
    vcf_out = VCFFileDirFmt()
    sleep(randint(0, 1))
    with open(vcf_out.path.joinpath("test.vcf"), 'w') as f_vcf:
        f_vcf.write("testing")

    return vcf_out
