#   Copyright 2022 Chase Ridenour
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
from q2_nasp2_types.alignment import AlignedReads
from q2_nasp2_types.snp import SNPFile, VCFFile
from q2_types.feature_data import Sequence, FeatureData
from qiime2.plugin import Plugin

import q2_snp_callers
from q2_snp_callers.actions.gatk.haplotype_caller import haplotype_caller

plugin = Plugin(name='snp-callers',
                version=q2_snp_callers.__version__,
                package='q2_snp_callers',
                website='https://github.com/TGenNorth/q2-snp-callers')

plugin.methods.register_function(
    function=haplotype_caller,
    inputs={'sequences': FeatureData[AlignedReads],
            'ref_genome': FeatureData[Sequence]
            },
    parameters={},
    outputs=[('output_vcf', SNPFile[VCFFile])],
    input_descriptions={
        'sequences': 'Reference sequences used to build bowtie2 index.',
        'ref_genome': ''},
    parameter_descriptions={},
    output_descriptions={'output_vcf': 'VCF file'}, #TODO: plurize the output
    name='Build bowtie2 index from reference sequences.',
    description='Build bowtie2 index from reference sequences.'
)
