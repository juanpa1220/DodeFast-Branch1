#include "SoftwareSerial.h"
SoftwareSerial serial_connection(10, 11);
#define BUFFER_SIZE 64
char inData[BUFFER_SIZE];
char inChar=-1;
int count=0;
int i=0;
const int LEDi=2;//I
const int LEDd=3;//D
const int LEDa=5;//A
const int LEDf=7;//F
const int LEDa2=8;//A
const int LEDb=13;//B





void setup()
{

  
  pinMode(LEDi,OUTPUT);
  pinMode(LEDd,OUTPUT);
  pinMode(LEDa,OUTPUT);
  pinMode(LEDf,OUTPUT);
  pinMode(LEDa2,OUTPUT);
  pinMode(LEDb,OUTPUT);


  Serial.begin(9600);
  serial_connection.begin(9600);
  serial_connection.println("Ready!!!");
  Serial.println("Started");
}
void loop()
{
 
  byte byte_count=serial_connection.available();
  if(byte_count)
  {
    Serial.println("Incoming Data");
    int first_bytes=byte_count;
    int remaining_bytes=0;
    if(first_bytes>=BUFFER_SIZE-1)
    {
      remaining_bytes=byte_count-(BUFFER_SIZE-1);
    }
    for(i=0;i<first_bytes;i++)
    {
      inChar=serial_connection.read();
      inData[i]=inChar;
    }
    inData[i]='\0';

    delay(100);



    if(String(inData)=="F")
    {
      Serial.println("Encontrò un F");
      digitalWrite(LEDf,HIGH);
      
      delay(5000);
      
      digitalWrite(LEDf,LOW);

      Serial.println("Apagar F");

      delay(2000);

      
      
      
    }
     else if(String(inData)=="DFA")
    {
      Serial.println("Encontrò un DFA");
      
      digitalWrite(LEDd,HIGH);
      
      digitalWrite(LEDf,HIGH);

      digitalWrite(LEDa2,HIGH);
      
      
      
      delay(5000);
      
      digitalWrite(LEDd,LOW);
      
      digitalWrite(LEDf,LOW);
      
      digitalWrite(LEDa2,LOW);

      Serial.println("Apagar DFA");

      delay(2000);
      
      
      
    }
         else if(String(inData)=="AF")
    {
      Serial.println("Encontrò un AF");
      
      digitalWrite(LEDa,HIGH);
      
      digitalWrite(LEDf,HIGH);

      
      
      
      
      delay(5000);
      
      digitalWrite(LEDa,LOW);
      
      digitalWrite(LEDf,LOW);
      


      Serial.println("Apagar AF");

      delay(2000);
      
      
      
    }
    else if(String(inData)=="IFA")
    {
      Serial.println("Encontrò un IFA");
      
      digitalWrite(LEDi,HIGH);

      
      digitalWrite(LEDf,HIGH);

      digitalWrite(LEDa2,HIGH);
      
      
      
      delay(5000);
      
      digitalWrite(LEDi,LOW);
      
      digitalWrite(LEDf,LOW);

      digitalWrite(LEDa2,LOW);
      


      Serial.println("Apagar IFA");

      delay(2000);
      
      
      
    }
    else if(String(inData)=="DFB")
    {
      Serial.println("Encontrò un DFB");
      
      digitalWrite(LEDd,HIGH);

      
      digitalWrite(LEDf,HIGH);

      digitalWrite(LEDb,HIGH);
      
      
      
      delay(5000);
      
      digitalWrite(LEDd,LOW);
      
      digitalWrite(LEDf,LOW);

      digitalWrite(LEDb,LOW);
      


      Serial.println("Apagar DFB");

      delay(2000);
      
      
      
    }

    else if(String(inData)=="IFB")
    {
      Serial.println("Encontrò un IFB");
      
      digitalWrite(LEDi,HIGH);

      
      digitalWrite(LEDf,HIGH);

      digitalWrite(LEDb,HIGH);
      
      
      
      delay(5000);
      
      digitalWrite(LEDi,LOW);
      
      digitalWrite(LEDf,LOW);

      digitalWrite(LEDb,LOW);
      


      Serial.println("Apagar DFB");

      delay(2000);
      
      
      
    }
    else if(String(inData)=="A")
    {
      Serial.println("Encontrò un A");
      
      digitalWrite(LEDa,HIGH);

 
      
      
      
      delay(5000);
      
      digitalWrite(LEDa,LOW);
      

      


      Serial.println("Apagar A");

      delay(2000);
      
      
      
    }
    else if(String(inData)=="DAA")
    {
      Serial.println("Encontrò un DAA");

      digitalWrite(LEDd,HIGH);
      digitalWrite(LEDa,HIGH);
      
      digitalWrite(LEDa2,HIGH);

 
      
      
      
      delay(5000);
      digitalWrite(LEDd,LOW);
      digitalWrite(LEDa,LOW);
      digitalWrite(LEDa2,LOW);
      

      


      Serial.println("Apagar A");

      delay(2000);
      
      
      
    }
        else if(String(inData)=="IAA")
    {
      Serial.println("Encontrò un IAA");

      digitalWrite(LEDi,HIGH);
      digitalWrite(LEDa,HIGH);
      
      digitalWrite(LEDa2,HIGH);

 
      
      
      
      delay(5000);
      digitalWrite(LEDi,LOW);
      digitalWrite(LEDa,LOW);
      digitalWrite(LEDa2,LOW);
      

      


      Serial.println("Apagar IAA");

      delay(2000);
      
      
      
    }
       else if(String(inData)=="DAB")
    {
      Serial.println("Encontrò un DAB");

      digitalWrite(LEDd,HIGH);
      digitalWrite(LEDa,HIGH);
      
      digitalWrite(LEDb,HIGH);

 
      
      
      
      delay(5000);
      digitalWrite(LEDd,LOW);
      digitalWrite(LEDa,LOW);
      digitalWrite(LEDb,LOW);
      

      


      Serial.println("Apagar DAB");

      delay(2000);
      
      
      
    }


       else if(String(inData)=="IAB")
    {
      Serial.println("Encontrò un DAB");

      digitalWrite(LEDi,HIGH);
      digitalWrite(LEDa,HIGH);
      
      digitalWrite(LEDb,HIGH);

 
      
      
      
      delay(5000);
      digitalWrite(LEDi,LOW);
      digitalWrite(LEDa,LOW);
      digitalWrite(LEDb,LOW);
      

      


      Serial.println("Apagar IAB");

      delay(2000);
      
      
      
    }

       else if(String(inData)=="AA")
    {
      Serial.println("Encontrò un AA");

      digitalWrite(LEDa,HIGH);
      digitalWrite(LEDa2,HIGH);
      
  

 
      
      
      
      delay(5000);
      digitalWrite(LEDa,LOW);
      digitalWrite(LEDa2,LOW);
   
      

      


      Serial.println("Apagar AA");

      delay(2000);
      
      
      
    }














    
    for(i=0;i<remaining_bytes;i++)
    {
      inChar=serial_connection.read();
    }
    Serial.println(inData);
   
    serial_connection.println("Se recibio: "+ String(inData));
    count++;//Increment the line counter
  }
  delay(100);//Pause for a moment 
}
