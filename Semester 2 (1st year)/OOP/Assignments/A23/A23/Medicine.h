#pragma once

typedef struct {
	char* name;
	int concentration;
	int quantity;
	float price;
}Medicine;

Medicine createMedicine(char* name, int concentration, int quantity, float price);

char* getName(Medicine medicine);
int getConcentration(Medicine medicine);
int getQuantity(Medicine medicine);
float getPrice(Medicine medicine);

void setName(Medicine* medicine, char* name);
void setConcentration(Medicine* medicine, int concentration);
void setQuantity(Medicine* medicine, int quantity);
void setPrice(Medicine* medicine, float price);

Medicine copyMedicine(Medicine medicine);

void destroyMedicine(Medicine medicine);
