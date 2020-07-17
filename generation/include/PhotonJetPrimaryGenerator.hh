#ifndef PhotonJetPrimaryGenerator_hh
#define PhotonJetPrimaryGenerator_hh 1

#include "G4VPrimaryGenerator.hh"

#include "G4SystemOfUnits.hh"
#include "globals.hh"

class G4Event;
class PhotonJetGeneratorMessenger;
class DetectorConstruction;
class G4Box;

class PhotonJetPrimaryGenerator : public G4VPrimaryGenerator
{
	public:
		PhotonJetPrimaryGenerator();
		virtual ~PhotonJetPrimaryGenerator();

	public:
		virtual void GeneratePrimaryVertex(G4Event*);

		void setMinPrimaryMomentum(G4double pMin) { minPrimaryMomentum = pMin; }
		void setMaxPrimaryMomentum(G4double pMax) { maxPrimaryMomentum = pMax; }
		void setSourcePosition(const G4ThreeVector& pos) { sourcePosition = pos; }
		void setParticleName(G4String name) { fParticleName = name; }

		G4double getMinPrimaryMomentum() const { return minPrimaryMomentum; }
		G4double getMaxPrimaryMomentum() const { return maxPrimaryMomentum; }
		G4ThreeVector getSourcePosition() const { return sourcePosition; }
		G4String getParticleName() const { return fParticleName; }

		static constexpr G4double default_minPrimaryMomentum = .01*GeV;
		static constexpr G4double default_maxPrimaryMomentum = 7.0*TeV;
		static constexpr G4double default_sourceDistance = 0.0*m;
		static const G4String default_particleName;

	private:
		PhotonJetGeneratorMessenger* fGeneratorMessenger;
		const G4Box* fDecayVolume;
		const G4Box* fPlane;
		const DetectorConstruction* fDetectorConstruction; 

		double minPrimaryMomentum;
		double maxPrimaryMomentum;
		G4ThreeVector sourcePosition;
		G4String fParticleName;
};
#endif
