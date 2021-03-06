import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP2Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
	comEnergy = cms.double(13000.0),
	filterEfficiency = cms.untracked.double(1),
	maxEventsToPrint = cms.untracked.int32(0),
	pythiaHepMCVerbosity = cms.untracked.bool(False),
	pythiaPylistVerbosity = cms.untracked.int32(1),
	PythiaParameters = cms.PSet(
            processParameters = cms.vstring(
                pythia8CommonSettingsBlock,
                pythia8CP2SettingsBlock,
                pythia8PSweightsSettingsBlock,
                
                'ExcitedFermion:dg2dStar = on',
                'ExcitedFermion:ug2uStar = on',
                'ExcitedFermion:Lambda = 2000',
                '4000001:m0 = 2000',
                '4000001:mWidth = 2',
                '4000001:onMode = off',
                '4000001:onIfMatch = 2 24',
                '4000002:m0 = 2000',
                '4000002:mWidth = 2',
                '4000002:onMode = off',
                '4000002:onIfMatch = 1 24',
                '24:m0 = 25',
                '24:mWidth = 0.625',
            ),
            parameterSets = cms.vstring('pythia8CommonSettings',
                                        'pythia8CP2Settings',
                                        'pythia8PSweightsSettings',
                                        'processParameters')
	)
)

ProductionFilterSequence = cms.Sequence(generator)
