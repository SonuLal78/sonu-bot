#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <unistd.h>

#define MAX_THREADS 100

typedef struct {
    char ip[100];
    int port;
    int duration;
} config_t;

void* worker(void* arg) {
    config_t* config = (config_t*)arg;
    printf("Connecting to %s:%d for %d seconds...\n", config->ip, config->port, config->duration);
    // यहाँ पर आप अपने बॉट या नेटवर्क लॉजिक जोड़ सकते हैं
    sleep(config->duration);
    printf("Finished connection to %s:%d\n", config->ip, config->port);
    pthread_exit(NULL);
}

int main() {
    char ip[100];
    int port, duration;
    pthread_t threads[MAX_THREADS];
    config_t configs[MAX_THREADS];

    printf("Enter IP: ");
    scanf("%s", ip);
    printf("Enter Port: ");
    scanf("%d", &port);
    printf("Enter Duration (seconds): ");
    scanf("%d", &duration);

    for (int i = 0; i < MAX_THREADS; i++) {
        strcpy(configs[i].ip, ip);
        configs[i].port = port;
        configs[i].duration = duration;
        int rc = pthread_create(&threads[i], NULL, worker, (void*)&configs[i]);
        if (rc) {
            printf("Error creating thread %d\n", i);
        }
    }

    for (int i = 0; i < MAX_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    printf("All threads completed.\n");
    return 0;
}
