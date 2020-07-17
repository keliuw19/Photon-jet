#include "PhotonJetPrimaryGenerator.hh"
#include "PhotonJetGeneratorMessenger.hh"
#include "Newaxion1.hh"
#include "Newaxion2.hh"
#include "G4LogicalVolumeStore.hh"
#include "G4Box.hh"
#include "DetectorConstruction.hh"
#include "G4RunManager.hh"
#include "Randomize.hh"
#include "G4PrimaryParticle.hh"
#include "CLHEP/Units/PhysicalConstants.h"
#include "G4Event.hh"

const G4String PhotonJetPrimaryGenerator::default_particleName = "Newaxion1";

PhotonJetPrimaryGenerator::PhotonJetPrimaryGenerator() 
	: G4VPrimaryGenerator(), fGeneratorMessenger(nullptr), fDecayVolume(nullptr), fDetectorConstruction(nullptr)
{
	fGeneratorMessenger = new PhotonJetGeneratorMessenger(this);
}

PhotonJetPrimaryGenerator::~PhotonJetPrimaryGenerator()
{
	delete fGeneratorMessenger;
}

void PhotonJetPrimaryGenerator::GeneratePrimaryVertex(G4Event* event)
{ 
	G4double decaySizeX = 0;
	G4double decaySizeY = 0;
	G4double decaySizeZ = 0;
	G4double planeSizeX = 0;
	G4double planeSizeY = 0;
	G4double decayLength = 0;

	G4bool firstCall = false;


	if ( fDetectorConstruction == nullptr )
	{
		fDetectorConstruction = static_cast<const DetectorConstruction*>(
				G4RunManager::GetRunManager()->GetUserDetectorConstruction());
	}


	G4double x0 = 2 * decaySizeX * (G4UniformRand() - 0.5);
	G4double y0 = 2 * decaySizeY * (G4UniformRand() - 0.5);
	G4double z0 = -decaySizeZ + 1.0*cm;

	G4ThreeVector position(x0, y0, z0);
	G4double time = 0.0 * s;
	G4PrimaryVertex* vertex = new G4PrimaryVertex(position, time);

	G4ThreeVector momentum = position - sourcePosition;

	if (firstCall) 
	{
		double solidAngleDecay = 4 * decaySizeX * decaySizeY * fabs(momentum.cosTheta()) / momentum.mag2();
		double solidAnglePlane = 4 * planeSizeX * planeSizeY * fabs(sourcePosition.cosTheta()) / sourcePosition.mag2();
		double geoWeight = solidAnglePlane / solidAngleDecay;
		G4cout << "Generator solid-angle factor: " << geoWeight << G4endl;
	}

	G4double logP = log(minPrimaryMomentum) + log(maxPrimaryMomentum/minPrimaryMomentum)*G4UniformRand();
	momentum.setMag(exp(logP));
	G4ParticleDefinition* particleDefinition = G4ParticleTable::GetParticleTable()->FindParticle(fParticleName);
	G4PrimaryParticle* primary = new G4PrimaryParticle(particleDefinition, momentum.x(), momentum.y(), momentum.z());

	// special logic to make dark photon decay point uniform over decay volume length
	if (fParticleName == "Newaxion1")
	{
		G4double decayProperTime = (1.0-G4UniformRand())*primary->GetMass()*decayLength/(primary->GetTotalMomentum() * CLHEP::c_light);
		//G4cout << "Proper time set for decay: " << decayProperTime / s << G4endl;
		primary->SetProperTime(decayProperTime);
	}
	vertex->SetPrimary(primary);
	event->AddPrimaryVertex(vertex);


}
