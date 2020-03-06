import tkinter as tk
from tkinter import ttk

countryList = ["US", "Mexico", "Switzerland", "Turkey", "Brazil", "Sudan", "Cambodia"]

# Create GUI
root = tk.Tk()
root.title("Expected Claim Calculator")
root.geometry('800x800')

sizeLbl = tk.Label(root, text="Number of individuals to be insured: ")
sizeLbl.grid(column=0, row=0)

sizeLbl = tk.Entry(root, width=10)
sizeLbl.insert(0, '1')
sizeLbl.grid(column=2, row=0)

countryLbl = tk.Label(root, text="Select a country: ")
countryLbl.grid(column=0, row=2)

calcButton = tk.Button(root, text="Calculate")
calcButton.configure(command=lambda:run())
calcButton.grid(column=3, row=7)

estimateLbl = tk.Label(root,text="")
estimateLbl.grid(column=4, row=5)

countrySelect = ttk.Combobox(root, values=countryList)
countrySelect.set("US")
countrySelect.grid(column=2,row=2)

# Input data

lowRiskDict = {"US":.01, "Mexico":.02, "Switzerland":.005, "Turkey":.011, "Brazil":.015, "Sudan":.022, "Cambodia":.022}
smokerOnlyDict = {"US":.02, "Mexico":.04, "Switzerland":.02, "Turkey":.03, "Brazil":.03, "Sudan":.04, "Cambodia":.05}
obeseOnlyDict = {"US":.015, "Mexico":.035, "Switzerland":.01, "Turkey":.019, "Brazil":.022, "Sudan":.038, "Cambodia":.045}
smokerAndObeseDict = {"US":.03, "Mexico":.08, "Switzerland":.03, "Turkey":.04, "Brazil":.055, "Sudan":.09, "Cambodia":.09}
avgClaimDict = {"US":100, "Mexico":157, "Switzerland":95, "Turkey":123, "Brazil":146, "Sudan":187, "Cambodia":199}
smokerPctDict = {"US":.2, "Mexico":.25, "Switzerland":.15, "Turkey":.31, "Brazil":.22, "Sudan":.14, "Cambodia":.37}
obesePctDict = {"US":.33, "Mexico":.38, "Switzerland":.21, "Turkey":.32, "Brazil":.27, "Sudan":.13, "Cambodia":.35}
smokerAndObesePctDict = {"US":.03, "Mexico":.08, "Switzerland":.03, "Turkey":.04, "Brazil":.055, "Sudan":.09, "Cambodia":.09}

# size = int(sizeLbl.get())
# country = str(countrySelect.get())

# Calculate expected claim amount
class expectedClaims():

# Likelihood of claim and percentage of group
    def risk(self,country):
        if country == "US":
            self.lowRiskFactor = lowRiskDict["US"]
        elif country == "Mexico":
            self.lowRiskFactor = lowRiskDict["Mexico"]
        elif country == "Switzerland":
            self.lowRiskFactor = lowRiskDict["Switzerland"]
        elif country == "Turkey":
            self.lowRiskFactor = lowRiskDict["Turkey"]
        elif country == "Brazil":
            self.lowRiskFactor = lowRiskDict["Brazil"]
        elif country == "Sudan":
            self.lowRiskFactor = lowRiskDict["Sudan"]
        elif country == "Cambodia":
            self.lowRiskFactor = lowRiskDict["Cambodia"]

        if country == "US":
            self.smokerOnlyRiskFactor = smokerOnlyDict["US"]
        elif country == "Mexico":
            self.smokerOnlyRiskFactor = smokerOnlyDict["Mexico"]
        elif country == "Switzerland":
            self.smokerOnlyRiskFactor = smokerOnlyDict["Switzerland"]
        elif country == "Turkey":
            self.smokerOnlyRiskFactor = smokerOnlyDict["Turkey"]
        elif country == "Brazil":
            self.smokerOnlyRiskFactor = smokerOnlyDict["Brazil"]
        elif country == "Sudan":
            self.smokerOnlyRiskFactor = smokerOnlyDict["Sudan"]
        elif country == "Cambodia":
            self.smokerOnlyRiskFactor = smokerOnlyDict["Cambodia"]

        if country == "US":
            self.obeseOnlyRiskFactor = obeseOnlyDict["US"]
        elif country == "Mexico":
            self.obeseOnlyRiskFactor = obeseOnlyDict["Mexico"]
        elif country == "Switzerland":
            self.obeseOnlyRiskFactor = obeseOnlyDict["Switzerland"]
        elif country == "Turkey":
            self.obeseOnlyRiskFactor = obeseOnlyDict["Turkey"]
        elif country == "Brazil":
            self.obeseOnlyRiskFactor = obeseOnlyDict["Brazil"]
        elif country == "Sudan":
            self.obeseOnlyRiskFactor = obeseOnlyDict["Sudan"]
        elif country == "Cambodia":
            self.obeseOnlyRiskFactor = obeseOnlyDict["Cambodia"]

        if country == "US":
            self.smokerAndObeseRiskFactor = smokerAndObeseDict["US"]
        elif country == "Mexico":
            self.smokerAndObeseRiskFactor = smokerAndObeseDict["Mexico"]
        elif country == "Switzerland":
            self.smokerAndObeseRiskFactor = smokerAndObeseDict["Switzerland"]
        elif country == "Turkey":
            self.smokerAndObeseRiskFactor = smokerAndObeseDict["Turkey"]
        elif country == "Brazil":
            self.smokerAndObeseRiskFactor = smokerAndObeseDict["Brazil"]
        elif country == "Sudan":
            self.smokerAndObeseRiskFactor = smokerAndObeseDict["Sudan"]
        elif country == "Cambodia":
            self.smokerAndObeseRiskFactor = smokerAndObeseDict["Cambodia"]

        if country == "US":
            self.smokerPct = smokerPctDict["US"]
        elif country == "Mexico":
            self.smokerPct = smokerPctDict["Mexico"]
        elif country == "Switzerland":
            self.smokerPct = smokerPctDict["Switzerland"]
        elif country == "Turkey":
            self.smokerPct = smokerPctDict["Turkey"]
        elif country == "Brazil":
            self.smokerPct = smokerPctDict["Brazil"]
        elif country == "Sudan":
            self.smokerPct = smokerPctDict["Sudan"]
        elif country == "Cambodia":
            self.smokerPct = smokerPctDict["Cambodia"]

        if country == "US":
            self.obesePct = obesePctDict["US"]
        elif country == "Mexico":
            self.obesePct = obesePctDict["Mexico"]
        elif country == "Switzerland":
            self.obesePct = obesePctDict["Switzerland"]
        elif country == "Turkey":
            self.obesePct = obesePctDict["Turkey"]
        elif country == "Brazil":
            self.obesePct = obesePctDict["Brazil"]
        elif country == "Sudan":
            self.obesePct = obesePctDict["Sudan"]
        elif country == "Cambodia":
            self.obesePct = obesePctDict["Cambodia"]

        if country == "US":
            self.smokerAndObesePct = smokerAndObesePctDict["US"]
        elif country == "Mexico":
            self.smokerAndObesePct = smokerAndObesePctDict["Mexico"]
        elif country == "Switzerland":
            self.smokerAndObesePct = smokerAndObesePctDict["Switzerland"]
        elif country == "Turkey":
            self.smokerAndObesePct = smokerAndObesePctDict["Turkey"]
        elif country == "Brazil":
            self.smokerAndObesePct = smokerAndObesePctDict["Brazil"]
        elif country == "Sudan":
            self.smokerAndObesePct = smokerAndObesePctDict["Sudan"]
        elif country == "Cambodia":
            self.smokerAndObesePct = smokerAndObesePctDict["Cambodia"]

        lowRiskPct = 1 - (self.smokerPct + self.obesePct + self.smokerAndObesePct)

        self.totalRiskFactor = (self.lowRiskFactor * (lowRiskPct)) + (self.smokerOnlyRiskFactor * (self.smokerPct)) + (self.obeseOnlyRiskFactor * (self.obesePct)) + (self.smokerAndObeseRiskFactor * (self.smokerAndObesePct))
        return (self.totalRiskFactor)

# Avg individual claim amount
    def claims(self,country):
        if country == "US":
            self.avgClaim = avgClaimDict["US"]
        elif country == "Mexico":
            self.avgClaim = avgClaimDict["Mexico"]
        elif country == "Switzerland":
            self.avgClaim = avgClaimDict["Switzerland"]
        elif country == "Turkey":
            self.avgClaim = avgClaimDict["Turkey"]
        elif country == "Brazil":
            self.avgClaim = avgClaimDict["Brazil"]
        elif country == "Sudan":
            self.avgClaim = avgClaimDict["Sudan"]
        elif country == "Cambodia":
            self.avgClaim = avgClaimDict["Cambodia"]
        return self.avgClaim

def run():
    size = int(sizeLbl.get())
    country = str(countrySelect.get())
    e = expectedClaims()
    totalClaims = (size * e.claims(country) * e.risk(country))
    estimateLbl['text'] = "Total expected claims = ", totalClaims
    print("Expected total claims: ", totalClaims)

root.mainloop()
