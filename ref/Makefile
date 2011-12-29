CFLAGS := -O2 -Wall -ggdb


test_Kasumi: test_Kasumi.c Kasumi.o
	gcc $(CFLAGS) $^ -o $@

Kasumi.o: Kasumi.c Kasumi.h
	gcc $(CFLAGS) $< -c -o $@


.PHONY: clean
clean:
	rm -f *.o test_Kasumi


