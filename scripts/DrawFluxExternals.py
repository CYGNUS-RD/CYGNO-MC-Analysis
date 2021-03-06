from ROOT import *
import os

#f = TFile.Open("output/neutron_50Water15Pb5Cu/out_external_neutron_50Water15Pb5Cu_merged.root")
#f = TFile.Open("output/neutrons_100Water5Cu/out_external_neutrons_100Water5Cu_merged.root")
#f = TFile.Open("output/neutrons_250Water5Cu/out_external_neutrons_250Water5Cu_merged.root")
#f = TFile.Open("output/neutrons_50Water15Pb5Cu/out_external_neutrons_50Water15Pb5Cu.root")
#f = TFile.Open("output/100Water5Cu_inputdist150Water/out_external_100Water5Cu_inputdist150Water.root")
#f0 = TFile.Open("output/gamma_100Water5Cu/out_external_gamma_100Water5Cu_merged.root")
#f0 = TFile.Open("output/50Water5Pb5Cu/out_external_50Water5Pb5Cu_merged.root")
#f = TFile.Open("output/neutrons_200Water5Cu/out_external_neutrons_200Water5Cu_merged.root")
#f0 = TFile.Open("output/neutrons_200Water5Cu/out_external_neutrons_200Water5Cu_merged.root")
#f = TFile.Open("output/neutrons_100Water5Cu_inputdist_100Water/out_external_neutrons_100Water5Cu_inputdist_100Water_merged.root")
#fg = TFile.Open("output/secondarygamma_100Water5Cu_inputdist100Water/out_external_secondarygamma_100Water5Cu_inputdist100Water_merged.root")
#f = TFile.Open("output/gamma_100Water5Cu/out_external_gamma_100Water5Cu_merged.root")
f = TFile.Open("output/50Water5Cu_inputdist150Water/out_external_50Water5Cu_inputdist150Water.root")
f0 = TFile.Open("output/gamma_100Water5Cu/out_external_gamma_100Water5Cu_merged.root")
#f= TFile.Open("output/gamma_50Water5Cu_inputdist50Water/out_external_gamma_50Water5Cu_inputdist50Water_merged.root")

outdir = "plots/"
os.system("mkdir -p "+outdir)

h = f.Get("h_edepDet_full_norm")
#h_NR = f.Get("h_edepDet_NR_full_norm")

#h_secondary = fg.Get("h_edepDet_full_norm")
#h_NR_secondary = fg.Get("h_edepDet_NR_full_norm")


#h_gs0 = fg.Get("h_EgammaShield0_full_norm") 
#h_gs1 = fg.Get("h_EgammaShield1_full_norm") 
#h_gs2 = fg.Get("h_EgammaShield2_full_norm") 
#h_gs3 = fg.Get("h_EgammaShield3_full_norm") 
#h_gsAirBox = fg.Get("h_EgammaAirBox_full_norm") 
#h_gs0.Scale(1./20)
#h_gs1.Scale(1./20)
#h_gs2.Scale(1./20)
#h_gs3.Scale(1./20)
#h_gsAirBox.Scale(1./20)
#
#h_secondary.Scale(1./20)
#h_NR_secondary.Scale(1./20)


h_g0 = f0.Get("h_EgammaShield0_full_norm") 
h_g0.Scale(1./39.)
#h_g0 = f.Get("h_EgammaShield0_full_norm") 
h_g1 = f.Get("h_EgammaShield1_full_norm") 
h_g2 = f.Get("h_EgammaShield2_full_norm") 
h_g3 = f.Get("h_EgammaShield3_full_norm") 
h_gAirBox = f.Get("h_EgammaAirBox_full_norm") 


#h_n0 = f0.Get("h_EneutronShield0_full_norm") 
#h_n0.Scale(1./84)
h_n0 = f.Get("h_EneutronShield0_full_norm") 
h_n1 = f.Get("h_EneutronShield1_full_norm") 
h_n2 = f.Get("h_EneutronShield2_full_norm") 
h_n3 = f.Get("h_EneutronShield3_full_norm") 
h_nAirBox = f.Get("h_EneutronAirBox_full_norm") 

n_finishedjobs = 1

h.Scale(1./n_finishedjobs) 
#h_NR.Scale(1./n_finishedjobs)

#h_g0.Scale(1./n_finishedjobs)
h_g1.Scale(1./n_finishedjobs)
h_g2.Scale(1./n_finishedjobs)
h_g3.Scale(1./n_finishedjobs)
h_gAirBox.Scale(1./n_finishedjobs)
h_n0.Scale(1./n_finishedjobs)
h_n1.Scale(1./n_finishedjobs)
h_n2.Scale(1./n_finishedjobs)
h_n3.Scale(1./n_finishedjobs)
h_nAirBox.Scale(1./n_finishedjobs)

#h.Add(h_secondary)
#h_NR.Add(h_NR_secondary)
#h_g0.Add(h_gs0)
#h_g1.Add(h_gs1)
#h_g2.Add(h_gs2)
#h_g3.Add(h_gs3)
#h_gAirBox.Add(h_gsAirBox)

leg = TLegend(0.3,0.7,0.65,0.85)
c_g =  TCanvas("c_g","",650,600)
c_g.SetLeftMargin(0.15)
c_g.cd()
c_g.SetLogy()
gStyle.SetPalette(57)
gStyle.SetOptStat(0)

h_g0.SetMaximum(10)
#h_g0.SetMaximum(1e-3)
h_g0.SetMinimum(1e-14)
h_g3.SetMaximum(1e-9)
h_g3.SetMinimum(1e-14)
h_g0.GetXaxis().SetTitle("Energy gamma [keV]")
h_g0.GetYaxis().SetTitle("Flux [#gamma/cm^{2}/s/keV]")
h_g1.GetXaxis().SetTitle("Energy gamma [keV]")
h_g1.GetYaxis().SetTitle("Flux [#gamma/cm^{2}/s/keV]")
h_g2.GetXaxis().SetTitle("Energy gamma [keV]")
h_g3.GetYaxis().SetTitle("Flux [#gamma/cm^{2}/s/keV]")
h_g2.GetXaxis().SetTitle("Energy gamma [keV]")
h_g3.GetYaxis().SetTitle("Flux [#gamma/cm^{2}/s/keV]")

h_g0.SetLineWidth(2)
h_g1.SetLineWidth(2)
h_g2.SetLineWidth(2)
h_g3.SetLineWidth(2)
h_gAirBox.SetLineWidth(2)

h_g0.GetXaxis().SetRangeUser(0,2800)
h_g0.Draw("PLC hist")
#h_g1.Draw("PLC hist_same")
#h_g2.Draw("PLC hist")
h_g3.Draw("PLC hist same")
h_gAirBox.Draw("PLC hist same")
leg.AddEntry(h_g0,"gamma flux @LNGS")
#leg.AddEntry(h_g1,"entering shield1")
#leg.AddEntry(h_g2,"pass water shield")
leg.AddEntry(h_g3,"pass 2m water shield")
leg.AddEntry(h_gAirBox,"pass 5cm Cu shield")
leg.Draw()
#c_g.SaveAs(outdir+"fluxGamma_external_neutrons_50Water15Pb5Cu.png")
#c_g.SaveAs(outdir+"fluxGamma_external_neutrons_250Water5Cu.png")
#c_g.SaveAs(outdir+"fluxGamma_external_neutrons_200Water5Cu.png")
#c_g.SaveAs(outdir+"fluxGamma_external_neutrons_200Water5Cu_2step.png")
#c_g.SaveAs(outdir+"fluxGamma_external_neutrons_100Water5Cu.png")
#c_g.SaveAs(outdir+"fluxGamma_100Water5Cu_2step.png")
#c_g.SaveAs(outdir+"fluxGamma_200Water5Cu.png")
c_g.SaveAs(outdir+"fluxGamma_200Water5Cu_2step.png")
c_g.SaveAs(outdir+"fluxGamma_200Water5Cu_2step.pdf")


leg_n = TLegend(0.3,0.75,0.65,0.85)
c_n =  TCanvas("c_n","",650,600)
c_n.SetLeftMargin(0.15)
c_n.cd()
c_n.SetLogy()
c_n.SetLogx()
gStyle.SetPalette(57)
gStyle.SetOptStat(0)

h_n0.GetXaxis().SetTitle("Energy neutron [keV]")
h_n0.GetYaxis().SetTitle("Flux [n/cm^{2}/s]")
h_n1.GetXaxis().SetTitle("Energy neutron [keV]")
h_n1.GetYaxis().SetTitle("Flux [n/cm^{2}/s]")
h_n2.GetXaxis().SetTitle("Energy neutron [keV]")
h_n2.GetYaxis().SetTitle("Flux [n/cm^{2}/s]")
h_n3.GetXaxis().SetTitle("Energy neutron [keV]")
h_n3.GetYaxis().SetTitle("Flux [n/cm^{2}/s]")
h_n0.SetMaximum(1e-3)
h_n0.SetMinimum(1e-15)

h_n0.SetLineWidth(2)
h_n1.SetLineWidth(2)
h_n2.SetLineWidth(2)
h_n3.SetLineWidth(2)
h_nAirBox.SetLineWidth(2)

h_n0.Draw("PLC hist")
#h_n1.Draw("PLC hist same")
#h_n2.Draw("PLC hist same")
h_n3.Draw("PLC hist same")
h_nAirBox.Draw("PLC hist same")
leg_n.AddEntry(h_n0,"neutron flux @LNGS")
#leg_n.AddEntry(h_n1,"entering shield1")
#leg_n.AddEntry(h_n2,"pass water shield")
leg_n.AddEntry(h_n3,"pass 2m water shield")
leg_n.AddEntry(h_nAirBox,"pass 5cm Cu shield")
leg_n.Draw()
#c_n.SaveAs(outdir+"fluxNeutron_external_neutrons_50Water15Pb5Cu.png")
#c_n.SaveAs(outdir+"fluxNeutron_external_neutrons_250Water5Cu.png")
#c_n.SaveAs(outdir+"fluxNeutron_external_neutrons_200Water5Cu.png")
#c_n.SaveAs(outdir+"fluxNeutron_external_neutrons_200Water5Cu_2step.png")
#c_n.SaveAs(outdir+"fluxNeutron_external_neutrons_200Water5Cu_2step.pdf")
#c_n.SaveAs(outdir+"fluxNeutron_external_neutrons_100Water5Cu.png")
#c_n.SaveAs(outdir+"fluxNeutrons_extGamma_100Water5Cu.png")
#c_n.SaveAs(outdir+"fluxNeutrons_extGamma_100Water5Cu_2step.png")
c_n.SaveAs(outdir+"fluxNeutrons_extGamma_200Water5Cu_2step.png")
c_n.SaveAs(outdir+"fluxNeutrons_extGamma_200Water5Cu_2step.pdf")

c = TCanvas("c","",650,600)
c.SetLeftMargin(0.15)
c.cd()
c.SetLogy(0)
h.SetLineWidth(1)
#h_NR.SetLineWidth(2)
#h_NR.SetLineColor(2)
leg_dep = TLegend(0.5,0.7,0.85,0.85)
leg_dep.SetLineColor(0)
leg_dep.AddEntry(h,"tot energy deposit")
#leg_dep.AddEntry(h_NR,"NR energy deposit")
h.GetXaxis().SetTitle("Energy deposit [keV]")
h.GetYaxis().SetTitle("Rate [cpd / kg / keV]")

h.GetXaxis().SetRangeUser(0,200)
h.SetTitle("")
#h_NR.SetTitle("")
h.Draw("")
#h_NR.Draw("same")
leg_dep.Draw()
c.SaveAs(outdir+"background_external_gamma_200Water5Cu_2step_zoom.png")
c.SaveAs(outdir+"background_external_gamma_200Water5Cu_2step_zoom.pdf")
#c.SaveAs(outdir+"background_external_neutrons_200Water5Cu_2step_zoom.png")
#c.SaveAs(outdir+"background_external_neutrons_200Water5Cu_2step_zoom.pdf")


h.Rebin(5)
h.Scale(1./5)
#h_NR.Rebin(5)
#h_NR.Scale(1./5)



h.GetXaxis().SetRangeUser(0,1000)
h.Draw("")
#h_NR.Draw("same")
leg_dep.Draw()
#c.SaveAs(outdir+"background_external_neutrons_50Water15Pb5Cu.png")
#c.SaveAs(outdir+"background_external_neutrons_250Water5Cu.png")
#c.SaveAs(outdir+"background_external_neutrons_200Water5Cu.png")
#c.SaveAs(outdir+"background_external_neutrons_200Water5Cu_2step.png")
#c.SaveAs(outdir+"background_external_neutrons_200Water5Cu_2step.pdf")
#c.SaveAs(outdir+"background_external_neutrons_100Water5Cu.png")
#c.SaveAs(outdir+"background_external_gamma_200Water5Cu.png")
#c.SaveAs(outdir+"background_external_gamma_100Water5Cu.png")
#c.SaveAs(outdir+"background_external_gamma_100Water5Cu_2step.png")
c.SaveAs(outdir+"background_external_gamma_200Water5Cu_2step.png")
c.SaveAs(outdir+"background_external_gamma_200Water5Cu_2step.pdf")

#----- keep the GUI alive ------------
if __name__ == '__main__':
  rep = ''
  while not rep in ['q','Q']:
    rep = raw_input('enter "q" to quit: ')
    if 1 < len(rep):
      rep = rep[0]
