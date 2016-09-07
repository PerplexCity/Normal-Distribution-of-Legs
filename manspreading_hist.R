library(ggplot2)
seats <- read.csv("~/Desktop/seats.csv")
bbi<-element_text(face="bold.italic", color="black")
asynch <-ggplot(data=seats, aes(seats$total)) +
  geom_histogram(binwidth=1, fill=I("lightblue"), col=I("black")) + 
  theme(legend.position='none', title=bbi) + 
  xlab("Occupancy") + ylab("Frequency") + 
  labs(title="Asynchronous Manspreaders") + 
  geom_vline(xintercept=mean(seats$total), linetype="longdash")+
  annotate("text", x=mean(seats$total)+1.35, y =1650, label=paste("mean = ", round(mean(seats$total),2) ))

synch <-ggplot(data=seats, aes(seats$adjtotal)) +
  geom_histogram(binwidth=1, fill=I("lightblue"), col=I("black")) + 
  theme(legend.position='none', title=bbi) + 
  xlab("Occupancy") + ylab("Frequency") + 
  labs(title="Synchronous Manspreaders") + 
  geom_vline(xintercept=mean(seats$adjtotal), linetype="longdash")+
  annotate("text", x=mean(seats$adjtotal)-1.35, y =2150, label=paste("mean = ", round(mean(seats$adjtotal), 2) ))