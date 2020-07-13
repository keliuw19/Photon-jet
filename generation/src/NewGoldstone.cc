#include "NewGoldstone.hh"
#include "G4ParticleTable.hh"
#include "G4PhysicalConstants.hh"
#include "G4SystemOfUnits.hh"
#include "G4DecayTable.hh"
#include "G4VDecayChannel.hh"
#include "G4PhaseSpaceDecayChannel.hh"
 
NewGoldstone* NewGoldstone::theGoldstone = nullptr;

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

NewGoldstone::NewGoldstone(
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
 
NewGoldstone::~NewGoldstone()
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

NewGoldstone* NewGoldstone::GoldstoneDefinition(G4double mass)
{    
   if(!theGoldstone) 
   {
     theGoldstone = new NewGoldstone(
				        "Goldstone",           mass,                   0,       0, 
				                                 0,                  -1,       -1,          
					                         0,                   0,        0,             
					                   "boson",                   0,        0,           135,
					                      false,                   0,     NULL);
     
     //create Decay Table
     G4DecayTable* table = new G4DecayTable();

     // create decay channel
     G4VDecayChannel* mode = new G4PhaseSpaceDecayChannel("Goldstone", 1.0, 2, "pi0", "pi0");
     table->Insert(mode);

     theGoldstone->SetDecayTable(table);
     
     G4cout << "Goldstone is created: m(MeV)= " 
            << theGoldstone->GetPDGMass()/MeV << G4endl;
  }
  return theGoldstone;
}
 
//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

NewGoldstone* NewGoldstone::Goldstone()
{    
   return theGoldstone;
} 
