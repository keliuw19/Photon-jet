#ifndef PhotonJetPhysicsMessenger_h
#define PhotonJetPhysicsMessenger_h 1

#include "G4UImessenger.hh"

class PhotonJetPhysicsList;
class G4UIdirectory;
class G4UIcmdWithADoubleAndUnit;

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
//
class PhotonJetPhysicsMessenger: public G4UImessenger
{
	public:
		PhotonJetPhysicsMessenger(PhotonJetPhysicsList* );
		virtual ~PhotonJetPhysicsMessenger();

		virtual void SetNewValue(G4UIcommand*, G4String);

	private:

		PhotonJetPhysicsList*          fPhysicsList;

		G4UIdirectory*             fPhysicsDir;

		G4UIcmdWithADoubleAndUnit* fDarkPhotonMassCmd;

};

#endif
