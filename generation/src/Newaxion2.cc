#include "Newaxion2.hh"
#include "G4ParticleTable.hh"
#include "G4PhysicalConstants.hh"
#include "G4SystemOfUnits.hh"
#include "G4DecayTable.hh"
#include "G4VDecayChannel.hh"
#include "G4PhaseSpaceDecayChannel.hh"
 
Newaxion2* Newaxion2::theaxion2 = nullptr;

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

Newaxion2::Newaxion2(
			          const G4String&     aName,        G4double            mass,
			          G4double            width,        G4double            charge,   
			          G4int               iSpin,        G4int               iParity,    
			          G4int               iConjugation, G4int               iIsospin,   
			          G4int               iIsospin3,    G4int               gParity,
			          const G4String&     pType,        G4int               lepton,      
			          G4int               baryon,       G4int               encoding,
			          G4bool              stable,       G4double            lifetime,
			          G4DecayTable        *decaytable)
              : G4ParticleDefinition( aName, mass, width, charge, iSpin, iParity,
		                      iConjugation, iIsospin, iIsospin3, gParity, pType,
			              lepton, baryon, encoding, stable, lifetime, decaytable )
{}
  
//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
 
Newaxion2::~Newaxion2()
{
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
//     
//    Arguments for constructor are as follows
//               name             mass          width         charge
//             2*spin           parity  C-conjugation
//          2*Isospin       2*Isospin3       G-parity
//               type    lepton number  baryon number   PDG encoding
//             stable         lifetime    decay table 
//
//

Newaxion2* Newaxion2::axion2Definition(G4double mass)
{    
   if(!theaxion2) 
   {
     theaxion2 = new Newaxion2(
				        "axion2",             mass,                   0,       0, 
				                                 0,                  -1,       +1,          
					                         0,                   0,        0,             
					                   "boson",                   0,        0,           10036,
					                      false,                   0,     NULL);
     
     //create Decay Table
     G4DecayTable* table = new G4DecayTable();

     // create decay channel
     G4VDecayChannel* mode = new G4PhaseSpaceDecayChannel("axion2", 1.0, 3, "pi0", "pi0", "pi0");
     table->Insert(mode);

     theaxion2->SetDecayTable(table);
     
     G4cout << "axion2 is created: m(MeV)= " 
            << theaxion2->GetPDGMass()/MeV << G4endl;
  }
  return theaxion2;
}
 
//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

Newaxion2* Newaxion2::axion2()
{    
   return theaxion2;
} 
