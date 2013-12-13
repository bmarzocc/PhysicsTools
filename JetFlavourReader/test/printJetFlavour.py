import FWCore.ParameterSet.Config as cms

process = cms.Process("testJET")
process.load("FWCore.MessageService.MessageLogger_cfi")

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/caf/user/bmarzocc/RadionToHHTo2G2B_M-300_TuneZ2star_8TeV-nm-madgraph_AODSIM_18.root')
)

process.printTree = cms.EDAnalyzer("ParticleListDrawer",
    src = cms.InputTag("genParticles"),
    maxEventsToPrint  = cms.untracked.int32(1)
)

process.myPartons = cms.EDProducer("PartonSelector",
    withLeptons = cms.bool(False),
    src = cms.InputTag("genParticles")
)

process.flavourByRef = cms.EDProducer("JetPartonMatcher",
    jets = cms.InputTag("ak5PFJets"),
    coneSizeToAssociate = cms.double(0.3),
    partons = cms.InputTag("myPartons")
)

process.flavourByVal = cms.EDProducer("JetFlavourIdentifier",
    srcByReference = cms.InputTag("flavourByRef"),
    physicsDefinition = cms.bool(False)
)

process.printEvent = cms.EDAnalyzer("printJetFlavour",
    srcSelectedPartons = cms.InputTag("myPartons"),
    srcByReference = cms.InputTag("flavourByRef"),
    srcByValue = cms.InputTag("flavourByVal")
)

process.printEventNumber = cms.OutputModule("AsciiOutputModule")

#process.TFileService = cms.Service("TFileService",
#    fileName = cms.string('prova.root')
#)

process.p = cms.Path(process.printTree*process.myPartons*process.flavourByRef*process.flavourByVal*process.printEvent)
process.outpath = cms.EndPath(process.printEventNumber)
process.MessageLogger.destinations = cms.untracked.vstring('cout','cerr')
#process.MessageLogger.cout = cms.PSet(
#    threshold = cms.untracked.string('ERROR')
#)


