import FWCore.ParameterSet.Config as cms

source = cms.Source("EmptySource")

from Configuration.Generator.PythiaUEZ2starSettings_cfi import *
generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(0.5),
    comEnergy = cms.double(8000.0),
    crossSection = cms.untracked.double(0.0218),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring(
            'PMAS(42,1)=550.0        ! LQ mass', 
            'IMSS(21)=33             ! LUN number for SLHA File (must be 33)', 
            'IMSS(22)=33             ! Read-in SLHA decay table', 
            'MSEL=0                  ! (D=1) to select between full user control (0, then use MSUB) and some preprogrammed alternative', 
            'MSUB(163)=1             ! g+g->LQ+LQbar', 
            'MSUB(164)=1             ! q+qbar->LQ+LQbar'),
        # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters',
            'SLHAParameters'),
        SLHAParameters = cms.vstring('SLHAFILE = Configuration/Generator/data/LQ_cmusnumu_beta0.5.out')
    )
)

munumujjFilter = cms.EDFilter("LQGenFilter",
    src        = cms.untracked.InputTag("generator"),
    eejj       = cms.bool(False),
    enuejj     = cms.bool(False),
    nuenuejj   = cms.bool(False),
    mumujj     = cms.bool(False),
    munumujj   = cms.bool(True),
    numunumujj = cms.bool(False)
)

configurationMetadata = cms.untracked.PSet(
        version = cms.untracked.string('$Revision: 1.3 $'),
        name = cms.untracked.string('$Source: /cvs/CMSSW/CMSSW/Configuration/GenProduction/python/PYTHIA6_Exotica_LQ_cmu_250_7TeV_munumujjFilter_cff.py,v $'),
        annotation = cms.untracked.string('default documentation string for PYTHIA6_Exotica_LQ_cmu_250_7TeV_munumujjFilter_cff.py')
)

ProductionFilterSequence = cms.Sequence(generator*munumujjFilter)
