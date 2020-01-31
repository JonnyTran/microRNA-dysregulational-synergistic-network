from __future__ import print_function, division, absolute_import

try:
    from .annotation import (
        Annotatable, GENCODE, MirBase, EnsemblGenes, RNAcentral, BioMartManager, GTEx, GeneOntology
    )

    from .interaction import (
        LncBase, MiRTarBase, TargetScan, LncRNA2Target, BioGRID, GeneMania, lncRInter, lncRNome, STRING
    )

    from .disease import (
        DisGeNet, HMDD, LncRNADisease, MalaCards
    )

except ImportError as e:
    msg = (
        "OpenOmics requirements are not installed.\n\n"
        "Please pip install as follows:\n\n"
        "  pip install openomics --upgrade  # or pip install"
    )
    raise ImportError(str(e) + "\n\n" + msg)
