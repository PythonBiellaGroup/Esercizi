#include <stdio.h>

#ifndef TRUE
#define TRUE 1
#endif
#ifndef FALSE
#define FALSE 0
#endif

static char Base, L, sL;

Solver(M)
   char *M;
{
   char n, m, bqn, bqm;
   char *nM, *pv, *vl;

   register char i, j, k;

   nM=(char *)malloc(L*L);
   pv=(char *)malloc(sL);
   vl=(char *)malloc(sL);

   for (i=0; i<L; i++){
      for (j=0; j<L; j++)
         if (*(M+i*L+j)==0)
            break;
      if (j<L)
        break;
   }

   if (i==L)
      return TRUE;

   n=i; m=j;

   for (i=0; i<sL; i++){
      *(pv+i)=TRUE;
      *(vl+i)=0;
   }

   for (i=0; i<L; i++){

      if (*(M+i*L+m)>0)
         *(pv+*(M+i*L+m))=FALSE;

      if (*(M+n*L+i)>0)
         *(pv+*(M+n*L+i))=FALSE;
   }
 
   bqn=n-(n%Base);
   bqm=m-(m%Base);

   for (i=bqn; i<bqn+Base; i++)
      for (j=bqm; j<bqm+Base; j++)
         if (*(M+i*L+j)>0)
            *(pv+*(M+i*L+j))=FALSE;

   for (i=1,j=0; i<sL-1; i++)
      if (*(pv+i)==TRUE){
         *(vl+j)=i;
         j++;
      }

   for (k=0; *(vl+k)>0; k++){

      for (i=0; i<L; i++)
         for (j=0; j<L; j++)
            *(nM+i*L+j)=*(M+i*L+j);
      
      *(nM+n*L+m)=*(vl+k);

      if (Solver(nM)){
         for (i=0; i<L; i++)
            for (j=0; j<L; j++)
               *(M+i*L+j)=*(nM+i*L+j);

         return TRUE;
      }
   }
   return FALSE;
}


main(argc, argv)
   int argc;
   char *argv[];

{
   char *M;
   register char i, j;


   Base=3;

   if (argc > 1){
     i=atoi(argv[1]);
     if (i<2 || i>8)
        printf("Wrong Base value %d, I'll use 3 instead...\n", i);
     else 
        Base=i;
   }

   L=Base*Base;
   sL=L+2;

   M=(char *)malloc(L*L);

   printf("Insert the matrix %dx%d, 0 if no value have been supplied.\n", L, L);
   
   for (i=0; i<L; i++)
      for (j=0; j<L; j++)
         scanf("%d", M+i*L+j);

   for (i=0; i<L; i++)
      for (j=0; j<L; j++)
         if (*(M+i*L+j)<0 || *(M+i*L+j)>L){
            printf("Input error %d\n", *(M+i*L+j));
            exit(1);
         }
 
   printf("\nProcessing input matrix: \n");

   for (i=0; i<L; i++){
      for (j=0; j<L; j++)
         printf("%2d ", *(M+i*L+j));
      printf("\n");
   }
   printf("\n");

   if (Solver(M)){
      printf(":-) Eureka :-)\n");
      for (i=0; i<L; i++){
         for (j=0; j<L; j++)
            printf("%2d ", *(M+i*L+j));
      printf("\n");
      }
   }
   else
      printf("Solution not found... :-(\n");

   exit(0);
}
