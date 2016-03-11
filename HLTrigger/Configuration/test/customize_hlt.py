from hlt_bph import *

process.source.fileNames          = cms.untracked.vstring([
    '/store/relval/CMSSW_8_0_0/RelValJpsiMuMu_Pt-15/GEN-SIM-RECO/80X_mcRun2_asymptotic_v4-v1/10000/CE6DB6EE-16DA-E511-91DF-0CC47A4D7650.root',
    '/store/relval/CMSSW_8_0_0/RelValJpsiMuMu_Pt-15/GEN-SIM-RECO/80X_mcRun2_asymptotic_v4-v1/10000/D4C6AFF6-15DA-E511-AFCC-0CC47A4D7666.root',
])
process.source.secondaryFileNames = cms.untracked.vstring([
    '/store/relval/CMSSW_8_0_0/RelValJpsiMuMu_Pt-15/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_v4-v1/10000/0A6E5D60-72D9-E511-972F-0CC47A4D7662.root',
    '/store/relval/CMSSW_8_0_0/RelValJpsiMuMu_Pt-15/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_v4-v1/10000/16364063-72D9-E511-BDA7-0CC47A4D7632.root',
    '/store/relval/CMSSW_8_0_0/RelValJpsiMuMu_Pt-15/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_v4-v1/10000/DA4C8E5D-72D9-E511-8F20-0025905B8560.root',
    '/store/relval/CMSSW_8_0_0/RelValJpsiMuMu_Pt-15/GEN-SIM-DIGI-RAW-HLTDEBUG/80X_mcRun2_asymptotic_v4-v1/10000/EE97E35D-72D9-E511-B442-0025905A610A.root',
])

process.maxEvents.input = cms.untracked.int32(-1)


process.theNtuples = cms.EDAnalyzer("BHltNtuples",
         
                       triggerResult            = cms.untracked.InputTag("TriggerResults::REHLT"),
                       triggerSummary           = cms.untracked.InputTag("hltTriggerSummaryAOD::REHLT"),
                       tagTriggerResult         = cms.untracked.InputTag("TriggerResults::HLT"),
                       tagTriggerSummary        = cms.untracked.InputTag("hltTriggerSummaryAOD::HLT"),

                       puInfoTag                = cms.untracked.InputTag("addPileupInfo"),
                       offlineVtx               = cms.InputTag("offlinePrimaryVertices"),
                       beamspot                 = cms.InputTag("offlineBeamSpot"),

                       genParticlesTag          = cms.untracked.InputTag("genParticles"),

                       L3CandidatesTag          = cms.InputTag("hltL3MuonCandidates"), 
                       TkCandidatesTag          = cms.InputTag("hltIter2DisplacedNRMuMuMerged"), 

                       MuMuVtxTag               = cms.untracked.InputTag("hltDisplacedmumuVtxProducerDoubleMu4LowMassNonResonant"),
                       TkVtxTag                 = cms.untracked.InputTag("hltLowMassNonResonantTkAllConeTracksIter"),

                       OfflineMuonsTag          = cms.untracked.InputTag("muons"),
                       OfflineTkTag             = cms.untracked.InputTag("generalTracks"),

                       thirdTrkMass             = cms.untracked.double(0.493677),# kaon
                       fourthTrkMass            = cms.untracked.double(0.139570),# pion
                       displacedJpsi            = cms.untracked.bool(False),

                       maxEta                   = cms.untracked.double(2.2),
                       minPtTrk                 = cms.untracked.double(0.5),
                       mind0Sign                = cms.untracked.double(0.),
                       doOffline                = cms.untracked.bool(True),
 
                       )   
                       

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("BHltNtuple.root"),
                                   closeFileFast = cms.untracked.bool(False)
                                   )

process.runAna = cms.EndPath(process.theNtuples)

