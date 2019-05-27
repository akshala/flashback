void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(8,INPUT); //8 camera1
  pinMode(7,INPUT); //7 camera2
  pinMode(4,INPUT); // Assign
  pinMode(6,INPUT); //Recall
  pinMode(5,INPUT); //Recall click

}
int count1=0;
int count2=0;
int count3=0;
int count4=0;
int count5=0;
void loop() {
  // put your main code here, to run repeatedly:
  int x=digitalRead(8);
  int y=digitalRead(7);
  int z=digitalRead(4);
  int a=digitalRead(6);
  int b=digitalRead(5);
  if (x==1){
    count1=1;}
  else if (x==0 && count1==1){
    Serial.println(1);
    count1=0;}
  if (y==1){
    count2=1;}
  else if (y==0 && count2==1){
    Serial.println(2);
    count2=0;}
  if (z==1){
    count3=1;}
  else if (z==0 && count3==1){
    Serial.println(3);
    count3=0;}
  if (a==1){
    count4=1;}
  else if (a==0 && count4==1){
    Serial.println(4);
    count4=0;}
  if (b==1){
    count5=1;}
  else if (b==0 && count5==1){
    Serial.println(5);
    count5=0;}
  else{
     Serial.println(8);
   }


}
