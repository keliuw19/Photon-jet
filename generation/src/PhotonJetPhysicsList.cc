#include "PhotonJetPhysicsList.hh"
#include "PhotonJetPhysicsMessenger.hh"
#include "G4SystemOfUnits.hh"
#include "G4UnitsTable.hh"

PhotonJetPhysicsList::PhotonJetPhysicsList() : G4VModularPhysicsList(), fDarkPhotonMass(default_darkPhoton_mass)
{ 
	G4cout << "Defining femtoCoulomb" << G4endl;                                                                                  
	new G4UnitDefinition("femtoCoulomb", "fC", "Electric charge", coulomb/1e15);                                                 

	fPhysicsMessenger = new PhotonJetPhysicsMessenger(this);
}

PhotonJetPhysicsList::~PhotonJetPhysicsList()
{
	if (fPhysicsMessenger != nullptr) delete fPhysicsMessenger;
}

void PhotonJetPhysicsList::ConstructParticle()
{
	G4cout << "PhotonJetPhysicsList::ConstructParticle() called" << G4endl;
	Newaxion1::axion1Definition(fDarkPhotonMass);
	G4VModularPhysicsList::ConstructParticle();
}

void PhotonJetPhysicsList::SetCuts()
{
	G4VModularPhysicsList::SetCuts();
}

void PhotonJetPhysicsList::ConstructProcess()
{
	G4VModularPhysicsList::ConstructProcess();
}
