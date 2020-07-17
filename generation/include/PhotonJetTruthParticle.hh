#ifndef PHOTONJETTRUTHPARTICLE_HH
#define PHOTONJETTRUTHPARTICLE_HH 1

#include "G4ThreeVector.hh"

class PhotonJetTruthParticle
{
	public:
		PhotonJetTruthParticle();
		PhotonJetTruthParticle(G4int trackID, G4int parentID, G4int pdgCode, G4ThreeVector vertex, 
				G4ThreeVector momentum, G4double energy);
		virtual ~PhotonJetTruthParticle();

		G4int TrackID() { return fTrackID; }
		G4int ParentID() { return fParentID; }
		G4int PdgCode() { return fPdgCode; }
		G4ThreeVector Vertex() { return fVertex; }
		G4ThreeVector Momentum() { return fMomentum; }
		G4double Energy() { return fEnergy; }

	private:
		G4int fTrackID;
		G4int fParentID;
		G4int fPdgCode;
		G4ThreeVector fVertex;
		G4ThreeVector fMomentum;
		G4double fEnergy;
};


#endif
