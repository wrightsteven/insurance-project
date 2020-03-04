import tkinter as tk

countryList = ["US", "Mexico", "Switzerland", "Turkey", "Brazil", "Sudan", "Cambodia"]

lowRiskDict = {"US":.01, "Mexico":.02, "Switzerland":.005, "Turkey":.011, "Brazil":.015, "Sudan":.022, "Cambodia":.022}
smokerOnlyDict = {"US":.02, "Mexico":.04, "Switzerland":.02, "Turkey":.03, "Brazil":.03, "Sudan":.04, "Cambodia":.05}
obeseOnlyDict = {"US":.015, "Mexico":.035, "Switzerland":.01, "Turkey":.019, "Brazil":.022, "Sudan":.038, "Cambodia":.045}
smokerAndObeseDict = {"US":.03, "Mexico":.08, "Switzerland":.03, "Turkey":.04, "Brazil":.055, "Sudan":.09, "Cambodia":.09}
avgClaimDict = {"US":100, "Mexico":157, "Switzerland":95, "Turkey":123, "Brazil":146, "Sudan":187, "Cambodia":199}

size = int(input("Enter number of individuals to be insured: "))
smokerOnly = int(input("Enter number of individuals who smoke but are not obese: "))
obeseOnly = int(input("Enter number of individuals who are obese but do not smoke: "))
smokerAndObese = int(input("Enter number of individuals who smoke and are obese: "))
lowRisk = size - (smokerAndObese + smokerOnly + obeseOnly)

country = (input("Please enter a country: "))

if country in countryList:
    country = country
else:
    country = input("Please enter a valid choice: ")

class expectedClaims():

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

        self.totalRiskFactor = (self.lowRiskFactor * (lowRisk/size)) + (self.smokerOnlyRiskFactor * (smokerOnly/size)) + (self.obeseOnlyRiskFactor * (obeseOnly/size)) + (self.smokerAndObeseRiskFactor * (smokerAndObese/size))
        return (self.totalRiskFactor)

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

e = expectedClaims()
totalClaims = (size * e.claims(country) * e.risk(country))
print(totalClaims)