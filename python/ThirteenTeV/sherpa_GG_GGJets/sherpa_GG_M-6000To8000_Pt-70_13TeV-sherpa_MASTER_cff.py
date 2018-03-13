import FWCore.ParameterSet.Config as cms
import os

source = cms.Source("EmptySource")

generator = cms.EDFilter("SherpaGeneratorFilter",
  maxEventsToPrint = cms.int32(0),
  filterEfficiency = cms.untracked.double(1.0),
  crossSection = cms.untracked.double(-1),
  SherpaProcess = cms.string('GG_M-6000To8000_Pt-70_13TeV-sherpa'),
  SherpackLocation = cms.string('./'),
  SherpackChecksum = cms.string('15a24ef1cbcc589a0b75c879b7f9c534'),
  FetchSherpack = cms.bool(False),
  SherpaPath = cms.string('./'),
  SherpaPathPiece = cms.string('./'),
  SherpaResultDir = cms.string('Result'),
  SherpaDefaultWeight = cms.double(1.0),
  SherpaParameters = cms.PSet(parameterSets = cms.vstring(
                             "MPI_Cross_Sections",
                             "Run"),
                              MPI_Cross_Sections = cms.vstring(
				" MPIs in Sherpa, Model = Amisic:",
				" semihard xsec = 39.5385 mb,",
				" non-diffractive xsec = 17.0318 mb with nd factor = 0.3142."
                                                  ),
                              Run = cms.vstring(
				" (run){",
				" EVENTS 100;",
				" EVENT_MODE HepMC;",
				" ME_SIGNAL_GENERATOR Amegic Internal;",
				" EVENT_GENERATION_MODE Unweighted;",
				" BEAM_1 2212; BEAM_ENERGY_1 6500.;",
				" BEAM_2 2212; BEAM_ENERGY_2 6500.;",
				" PDF_LIBRARY LHAPDFSherpa;",
				" PDF_SET NNPDF30_nnlo_as_0118;",
				" FINISH_OPTIMIZATION Off;",
				" CSS_EW_MODE 1;",
				" ME_QED Off;",
				"}(run)",
				" (processes){",
				" Process 21 21 -> 22 22;",
				" Scales VAR{Abs2(p[2]+p[3])};",
				" ME_Generator Internal;",
				" Loop_Generator gg_yy;",
				" End process;",
				" Process 93 93 -> 22 22;",
				" Order (*,2);",
				" CKKW sqr(20./E_CMS);",
				" End process;",
				"}(processes)",
				" (selector){",
				" Mass 22 22 6000. 8000.;",
				" PT 22 70. E_CMS;",
				" PseudoRapidity 22 -2.8 2.8;",
				"}(selector)"                                                  ),
                             )
)

ProductionFilterSequence = cms.Sequence(generator)

