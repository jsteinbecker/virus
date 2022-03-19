class virus :
   
   def __init__(self,balti_class) -> None:
      self.balti = balti_class
      
      if "+" in self.balti :
         self.polarity = "Positive"
      if "-" in self.balti :
         self.polarity = "Negative"
      if "ds" in self.balti :
         self.polarity = "NA (double-stranded)"
      
      if "RNA" in self.balti :
         self.genType = "RNA"
      if "DNA" in self.balti :
         self.genType = "DNA"
      
          
coV = virus("+ssRNA")
coV.polarity
coV.genType

herpes = virus("dsDNA")
herpes.polarity

viruses = {"coronaviridae" : coV,
           "herpesviridae" : herpes}
