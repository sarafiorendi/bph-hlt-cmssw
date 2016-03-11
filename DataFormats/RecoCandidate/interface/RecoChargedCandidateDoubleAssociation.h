#ifndef BTauReco_RecoChargedCandidateDoubleAssociation_h
#define BTauReco_RecoChargedCandidateDoubleAssociation_h
// \class RecoChargedCandidateDoubleAssociation
// 
// \short association of double to a RecoChargedCandidate
// 

#include "DataFormats/RecoCandidate/interface/RecoChargedCandidateFwd.h"
#include <vector>

namespace reco {

  typedef std::pair<reco::RecoChargedCandidateRef, reco::RecoChargedCandidateRef >  TwoChargedCandidatePair;
  typedef std::pair<TwoChargedCandidatePair, double >                               RecoChargedCandidatesDoublePair;
  typedef std::vector<std::pair<TwoChargedCandidatePair, double > >                 RecoChargedCandidatesDoubleMap ;

  typedef std::pair<reco::RecoChargedCandidateRef, double >                         RecoChargedCandidateDoublePair;
  typedef std::vector<std::pair<reco::RecoChargedCandidateRef, double > >           RecoChargedCandidateDoubleMap ;


  typedef std::vector<std::pair<double, float > >              dfVector;
  typedef std::pair<double, float >                            dfPair;
}
#endif