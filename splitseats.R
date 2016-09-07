splitseats <- read.csv("~/Desktop/splitseats.csv", sep="")
bbi<-element_text(face="bold.italic", color="black")
split <-ggplot(data=splitseats, aes(splitseats$total)) +
  geom_histogram(binwidth=1, fill=I("lightblue"), col=I("black")) + 
  theme(legend.position='none', title=bbi) + 
  xlab("Occupancy") + ylab("Frequency") + 
  labs(title="Segregated Manspreaders") + 
  geom_vline(xintercept=mean(splitseats$total), linetype="longdash")+
  annotate("text", x=mean(splitseats$total)+3, y =4250, label=paste("mean = ", round(mean(splitseats$total),2) ))
