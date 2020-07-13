#ifndef Newaxion1_hh
#define Newaxion1_hh 1

#include "G4ParticleDefinition.hh"
#include "G4SystemOfUnits.hh"
#include "globals.hh"

class Newaxion1 : public G4ParticleDefinition
{
private:
  static Newaxion1* theaxion1;

  Newaxion1(
	           const G4String&     aName,        G4double            mass,
	           G4double            width,        G4double            charge,   
	           G4int               iSpin,        G4int               iParity,    
	           G4int               iConjugation, G4int               iIsospin,   
	           G4int               iIsospin3,    G4int               gParity,
	           const G4String&     pType,        G4int               lepton,      
	           G4int               baryon,       G4int               encoding,
	           G4bool              stable,       G4double            lifetime,
	           G4DecayTable        *decaytable );

  virtual ~Newaxion1();

public:

  static Newaxion1* axion1Definition( G4double mass );

  static Newaxion1* axion1( );

};
#endif
