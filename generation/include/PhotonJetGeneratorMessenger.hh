#ifndef PhotonJetGeneratorMessenger_h
#define PhotonJetGeneratorMessenger_h 1

#include "G4UImessenger.hh"
#include "globals.hh"

class PhotonJetPrimaryGenerator;
class G4UIdirectory;
class G4UIcommand;
class G4UIcmdWithADoubleAndUnit;
class G4UIcmdWith3VectorAndUnit;
class G4UIcmdWithoutParameter;
class G4UIcmdWithAString;

class PhotonJetGeneratorMessenger : public G4UImessenger
{
	public:
		PhotonJetGeneratorMessenger(PhotonJetPrimaryGenerator* primaryGenerator);
		~PhotonJetGeneratorMessenger();

	public:
		virtual void SetNewValue(G4UIcommand* command, G4String newValues);
		virtual G4String GetCurrentValue(G4UIcommand* command);

	private:
		PhotonJetPrimaryGenerator* fPrimaryGenerator;

	private:
		G4UIdirectory*                 generatorDirectory;
		G4UIcmdWithADoubleAndUnit*     cmd_gen_minPrimaryMomentum;
		G4UIcmdWithADoubleAndUnit*     cmd_gen_maxPrimaryMomentum;
		G4UIcmdWith3VectorAndUnit*     cmd_gen_sourcePosition;
		G4UIcmdWithoutParameter*       cmd_gen_dump;
		G4UIcmdWithAString*            cmd_gen_particle;
};

#endif
