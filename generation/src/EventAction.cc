//
// ********************************************************************
// * License and Disclaimer                                           *
// *                                                                  *
// * The  Geant4 software  is  copyright of the Copyright Holders  of *
// * the Geant4 Collaboration.  It is provided  under  the terms  and *
// * conditions of the Geant4 Software License,  included in the file *
// * LICENSE and available at  http://cern.ch/geant4/license .  These *
// * include a list of copyright holders.                             *
// *                                                                  *
// * Neither the authors of this software system, nor their employing *
// * institutes,nor the agencies providing financial support for this *
// * work  make  any representation or  warranty, express or implied, *
// * regarding  this  software system or assume any liability for its *
// * use.  Please see the license in the file  LICENSE  and URL above *
// * for the full disclaimer and the limitation of liability.         *
// *                                                                  *
// * This  code  implementation is the result of  the  scientific and *
// * technical work of the GEANT4 collaboration.                      *
// * By using,  copying,  modifying or  distributing the software (or *
// * any work based  on the software)  you  agree  to acknowledge its *
// * use  in  resulting  scientific  publications,  and indicate your *
// * acceptance of all terms of the Geant4 Software license.          *
// ********************************************************************
//
// $Id: EventAction.cc 75604 2013-11-04 13:17:26Z gcosmo $
// 
/// \file EventAction.cc
/// \brief Implementation of the EventAction class

#include "EventAction.hh"
#include "RunData.hh"

#include "G4RunManager.hh"
#include "G4Event.hh"
#include "G4UnitsTable.hh"

#include "Randomize.hh"
#include <iomanip>

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

EventAction::EventAction()
 : G4UserEventAction()
{}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

EventAction::~EventAction()
{}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

void EventAction::PrintEventStatistics(
                              G4double absoEdep, G4double absoTrackLength,
                              G4double gapEdep, G4double gapTrackLength) const
{
  // print event statistics
  G4cout
     << "   Absorber: total energy: " 
     << std::setw(7) << G4BestUnit(absoEdep, "Energy")
     << "       total track length: " 
     << std::setw(7) << G4BestUnit(absoTrackLength, "Length")
     << G4endl
     << "        Gap: total energy: " 
     << std::setw(7) << G4BestUnit(gapEdep, "Energy")
     << "       total track length: " 
     << std::setw(7) << G4BestUnit(gapTrackLength, "Length")
     << G4endl;
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

void EventAction::BeginOfEventAction(const G4Event* /*event*/)
{  
  RunData* runData 
    = static_cast<RunData*>(
        G4RunManager::GetRunManager()->GetNonConstCurrentRun());
  runData->Reset();  
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

void EventAction::EndOfEventAction(const G4Event* event)
{
	G4cout<<"EndofEventAction"<<G4endl;
  RunData* runData 
    = static_cast<RunData*>(
        G4RunManager::GetRunManager()->GetNonConstCurrentRun());
  G4PrimaryVertex* primaryVertex = event->GetPrimaryVertex();
  G4PrimaryParticle* primaryParticle = primaryVertex->GetPrimary();
  G4double ke = primaryParticle->GetKineticEnergy()/1000.; //in GeV.
  G4double px_mom = primaryParticle->GetPx()/1000.; //in GeV.
  G4double py_mom = primaryParticle->GetPy()/1000.; //in GeV.
  G4double pz_mom = primaryParticle->GetPz()/1000.; //in GeV.
  G4int pdg_mom=primaryParticle->GetPDGcode();
  G4cout<<primaryParticle->pdg_mom<<G4endl;

  G4PrimaryParticle* dau = primaryParticle->GetDaughter();
  if(dau!=nullptr){
  G4double ke_dau1 = dau->GetKineticEnergy()/1000.; //in GeV.
  G4double px_dau1 = dau->GetPx()/1000.; //in GeV.
  G4double py_dau1 = dau->GetPy()/1000.; //in GeV.
  G4double pz_dau1 = dau->GetPz()/1000.; //in GeV.
  G4int pdg_dau1=dau->GetPDGcode();

  runData->SetDaughter1(ke_dau1,px_dau1,py_dau1,pz_dau1,pdg_dau1);
  if(dau->GetNext()!=nullptr){
  G4double ke_dau2 = dau->GetNext()->GetKineticEnergy()/1000.; //in GeV.
  G4double px_dau2 = dau->GetNext()->GetPx()/1000.; //in GeV.
  G4double py_dau2 = dau->GetNext()->GetPy()/1000.; //in GeV.
  G4double pz_dau2 = dau->GetNext()->GetPz()/1000.; //in GeV.
  G4int pdg_dau2=dau->GetNext()->GetPDGcode();
  runData->SetDaughter2(ke_dau2,px_dau2,py_dau2,pz_dau2,pdg_dau2);
  }
  }

  runData->SetTotalEnergy(ke);
  runData->SetMomentum(px_mom,py_mom,pz_mom,pdg_mom);
  runData->FillPerEvent();
  
  //print per event (modulo n)
  //
  G4int eventID = event->GetEventID();
  G4int printModulo = G4RunManager::GetRunManager()->GetPrintProgress();
  // if ( ( printModulo > 0 ) && ( eventID % printModulo == 0 ) ) {
  //   G4cout << "---> End of event: " << eventID << G4endl;     

  //   PrintEventStatistics(
  //     runData->GetEdep(kAbs),
  //     runData->GetTrackLength(kAbs),
  //     runData->GetEdep(kGap),
  //     runData->GetTrackLength(kGap));
  // }
}  

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
