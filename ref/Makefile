CFLAGS := -O2 -Wall -ggdb


test_kasumi: test_kasumi.c kasumi.o
	gcc $(CFLAGS) $^ -o $@

kasumi.o: kasumi.c kasumi.h
	gcc $(CFLAGS) $< -c -o $@


.PHONY: clean
clean:
	rm -f *.o test_kasumi


