#ifndef Newaxion2_hh
#define Newaxion2_hh 1

#include "G4ParticleDefinition.hh"
#include "G4SystemOfUnits.hh"
#include "globals.hh"

class Newaxion2 : public G4ParticleDefinition
{
private:
  static Newaxion2* theaxion2;

  Newaxion2(
	           const G4String&     aName,        G4double            mass,
	           G4double            width,        G4double            charge,   
	           G4int               iSpin,        G4int               iParity,    
	           G4int               iConjugation, G4int               iIsospin,   
	           G4int               iIsospin3,    G4int               gParity,
	           const G4String&     pType,        G4int               lepton,      
	           G4int               baryon,       G4int               encoding,
	           G4bool              stable,       G4double            lifetime,
	           G4DecayTable        *decaytable );

  virtual ~Newaxion2();

public:

  static Newaxion2* axion2Definition( G4double mass );

  static Newaxion2* axion2( );

};
#endif
