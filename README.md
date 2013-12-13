PhysicsTools
============

1) JetFlavourReader:
    
    Vary simple analyzer (JetFlavourReader/plugins/printJetFlavour.cc) exploting CMSSW tools:
    
    SimDataFormats/JetMatching/interface/JetFlavour.h
    SimDataFormats/JetMatching/interface/JetFlavourMatching.h
    SimDataFormats/JetMatching/interface/MatchedPartons.h
    SimDataFormats/JetMatching/interface/JetMatchedPartons.h
    
    it can be launched in local by means of: JetFlavourReader/test/printJetFlavour.py
    or be launched in grid by means of: JetFlavourReader/test/crab/crab_printJetFlavour.cfg
    
    This analyzer can run on AODSIM format.
    
    The output is a txt. For each jet it'w written:
    
    event_luminosy - event_id - jet_pt jet - jet_eta - jet_phi - jet_energy - jet_flavour - #_processed_jet - #_processed_jet with flavour != 0
    
    If you want to have h2globe read the output, in order to fill the flattrees jet_flavour branch, you must put it
    in /afs/cern.ch/work/b/bmarzocc/public/RadionAnalysis_DONOTREMOVE/. Be careful to the output name! 
