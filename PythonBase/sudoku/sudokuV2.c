#include <stdio.h>

#ifndef TRUE
#define TRUE 1
#endif
#ifndef FALSE
#define FALSE 0
#endif

#define ORDER 3
#define SIDE ORDER*ORDER
#define LIST SIDE+2

Solver(M)
   char M[SIDE][SIDE];
{
   char n, m, bqn, bqm;
   char nM[SIDE][SIDE], pv[LIST], vl[LIST];

   register char i, j, k;

   for (i=0; i<SIDE; i++){

      for (j=0; j<SIDE; j++)
         if (M[i][j]==0)
            break;

      if (j<SIDE)
        break;
   }

   if (i==SIDE)
      return TRUE;

   n=i; m=j;

   for (i=0; i<LIST; i++){
      pv[i]=TRUE;
      vl[i]=0;
   }

   for (i=0; i<SIDE; i++){

      if (M[i][m]>0)
         pv[M[i][m]]=FALSE;

      if (M[n][i]>0)
         pv[M[n][i]]=FALSE;
   }
 
   bqn=n-(n%ORDER);
   bqm=m-(m%ORDER);

   for (i=bqn; i<bqn+ORDER; i++)
      for (j=bqm; j<bqm+ORDER; j++)
         if (M[i][j]>0)
            pv[M[i][j]]=FALSE;

   for (i=1,j=0; i<LIST-1; i++)
      if (pv[i]==TRUE)
         vl[j++]=i;

   for (k=0; vl[k]>0; k++){

      for (i=0; i<SIDE; i++)
         for (j=0; j<SIDE; j++)
            nM[i][j]=M[i][j];
      
      nM[n][m]=vl[k];

      if (Solver(nM)){
         for (i=0; i<SIDE; i++)
            for (j=0; j<SIDE; j++)
               M[i][j]=nM[i][j];

         return TRUE;
      }
   }
   return FALSE;
}


main(argc, argv)
   int argc;
   char *argv[];

{
   char M[SIDE][SIDE];
   register char i, j;

   printf("Insert the matrix %dx%d, 0 if no value have been supplied.\n", SIDE, SIDE);
   
   for (i=0; i<SIDE; i++)
      for (j=0; j<SIDE; j++)
         scanf("%d",&M[i][j]);

   for (i=0; i<SIDE; i++)
      for (j=0; j<SIDE; j++)
         if (M[i][j]<0 || M[i][j]>SIDE){
            printf("Input error %d\n", M[i][j]);
            exit(1);
         }
 
   printf("\nProcessing input matrix: \n");

   for (i=0; i<SIDE; i++){
      for (j=0; j<SIDE; j++)
         printf("%2d ", M[i][j]);
      printf("\n");
   }
   printf("\n");

   if (Solver(M)){
      printf("Solution found...\n");
      for (i=0; i<SIDE; i++){
         for (j=0; j<SIDE; j++)
            printf("%2d ", M[i][j]);
      printf("\n");
      }
   }
   else
      printf("Solution not found...\n");

   exit(0);
}
