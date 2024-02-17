#include <stdio.h>
#include <SDL2/SDL.h>

#define SCREEN_WIDTH 640
#define SCREEN_HEIGHT 480

// Define the map - numbers represent different types of walls
int map[SCREEN_WIDTH][SCREEN_HEIGHT] = {
    {1, 1, 1, 1, 1, 1, 1, 1},
    {1, 0, 0, 0, 0, 0, 0, 1},
    {1, 0, 1, 0, 1, 0, 1, 1},
    {1, 0, 0, 0, 0, 0, 0, 1},
    {1, 1, 1, 1, 1, 1, 1, 1}
};

double playerAngle = 0.0; // Initial angle of the camera

void drawWalls(SDL_Renderer *renderer) {
    for (int x = 0; x < SCREEN_WIDTH; x++) {
        // Calculate the direction of the ray
        double rayAngle = (playerAngle - 30) + (60 * ((double) x / (double) SCREEN_WIDTH));
        
        // Calculate distance to walls (simple demonstration)
        double distanceToWall = 0; // Replace with actual distance calculation

        // Determine wall and floor/ceiling colors
        int wallColor, floorCeilingColor;
        if (map[x][0] == 1) {
            wallColor = 0; // Color for walls
            floorCeilingColor = 255; // Color for floor/ceiling
        } else {
            wallColor = 255; // Color for walls
            floorCeilingColor = 0; // Color for floor/ceiling
        }

        // Draw the walls
        SDL_SetRenderDrawColor(renderer, wallColor, wallColor, wallColor, 255);
        SDL_RenderDrawLine(renderer, x, SCREEN_HEIGHT / 2 - distanceToWall / 2, x, SCREEN_HEIGHT / 2 + distanceToWall / 2);

        // Draw the floor and ceiling
        SDL_SetRenderDrawColor(renderer, floorCeilingColor, floorCeilingColor, floorCeilingColor, 255);
        SDL_RenderDrawLine(renderer, x, 0, x, SCREEN_HEIGHT / 2 - distanceToWall / 2);
        SDL_RenderDrawLine(renderer, x, SCREEN_HEIGHT / 2 + distanceToWall / 2, x, SCREEN_HEIGHT);
    }
}

int main(int argc, char *argv[]) {
    // SDL initialization
    if (SDL_Init(SDL_INIT_VIDEO) != 0) {
        printf("SDL initialization failed: %s\n", SDL_GetError());
        return 1;
    }

    // Create a window and renderer
    SDL_Window *window = SDL_CreateWindow("Raycasting Demo", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, SCREEN_WIDTH, SCREEN_HEIGHT, 0);
    SDL_Renderer *renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);

    if (window == NULL || renderer == NULL) {
        printf("Failed to create window or renderer: %s\n", SDL_GetError());
        return 1;
    }

    // Set the render color to white
    SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);

    // Main loop for drawing walls
    int isRunning = 1;
    SDL_Event event;
    while (isRunning) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                isRunning = 0;
            }
        }

        // Modify player angle (for testing purposes)
        playerAngle += 0.01;

        // Clear the window
        SDL_RenderClear(renderer);

        // Draw walls using raycasting
        drawWalls(renderer);

        // Render the changes
        SDL_RenderPresent(renderer);
    }

    // Clean up and exit
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
    
    return 0;
}
