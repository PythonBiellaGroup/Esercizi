#include <stdio.h>

#ifndef TRUE
#define TRUE 1
#endif
#ifndef FALSE
#define FALSE 0
#endif


Solver(M)
   char M[9][9];
{
   char n, m, bqn, bqm;
   char nM[9][9], pv[11], vl[11];

   register char i, j, k;

   for (i=0; i<9; i++){

      for (j=0; j<9; j++)
         if (M[i][j]==0)
            break;

      if (j<9)
        break;
   }

   if (i==9)
      return TRUE;

   n=i; m=j;

   for (i=0; i<12; i++){
      pv[i]=TRUE;
      vl[i]=0;
   }

   for (i=0; i<9; i++){

      if (M[i][m]>0)
         pv[M[i][m]]=FALSE;

      if (M[n][i]>0)
         pv[M[n][i]]=FALSE;
   }
 
   bqn=n-(n%3);
   bqm=m-(m%3);

   for (i=bqn; i<bqn+3; i++)
      for (j=bqm; j<bqm+3; j++)
         if (M[i][j]>0)
            pv[M[i][j]]=FALSE;

   for (i=1,j=0; i<10; i++)
      if (pv[i]==TRUE)
         vl[j++]=i;

   for (k=0; vl[k]>0; k++){

      for (i=0; i<9; i++)
         for (j=0; j<9; j++)
            nM[i][j]=M[i][j];
      
      nM[n][m]=vl[k];

      if (Solver(nM)){
         for (i=0; i<9; i++)
            for (j=0; j<9; j++)
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
   char M[9][9];
   register char i, j;

   printf("Insert the matrix 9x9, 0 if no value have been supplied.\n");
   
   for (i=0; i<9; i++)
      for (j=0; j<9; j++)
         scanf("%d",&M[i][j]);

   for (i=0; i<9; i++)
      for (j=0; j<9; j++)
         if (M[i][j]<0 || M[i][j]>9){
            printf("Input error %d\n", M[i][j]);
            exit(1);
         }
 
   printf("\nProcessing input matrix: \n");

   for (i=0; i<9; i++){
      for (j=0; j<9; j++)
         printf("%d ", M[i][j]);
      printf("\n");
   }
   printf("\n");

   if (Solver(M)){
      printf("Solution found...\n");
      for (i=0; i<9; i++){
         for (j=0; j<9; j++)
            printf("%d ", M[i][j]);
      printf("\n");
      }
   }
   else
      printf("Solution not found...\n");

   exit(0);
}
