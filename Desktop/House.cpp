#include<stdio.h>
#include<graphics.h>
int main()
{
	int gd=DETECT,gm;
	initgraph(&gd,&gm,(char*)"");
	// Draw house
	rectangle(300,300,900,600);
	rectangle(400,400,500,600);
	line(275,200,300,300);
	line(250,250,275,200);
	line(250,250,300,300);
	line(900,300,875,200);
	line(875,200,275,200);
	line(250,550,300,600);
	line(250,550,250,250);
	//Fill colors
	setfillstyle(SOLID_FILL, BROWN);
	floodfill(305,305, WHITE);
	floodfill(402,402, WHITE);
	setfillstyle(SLASH_FILL,BROWN);
	floodfill(402,402, WHITE);
 	setfillstyle(HATCH_FILL, GREEN);
 	floodfill(255,255, WHITE);
	floodfill(300,250, WHITE);
	setfillstyle(SOLID_FILL,BLUE);
	floodfill(260,460,WHITE);
	setfillstyle(SOLID_FILL,WHITE);
	floodfill(260,250,WHITE);
	getch();
	closegraph();
	return 0;
	}
