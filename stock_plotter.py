###
### Author: Kevin Cascais Nisterenko
### Course: CSc 110
### Description: My program/solution to Stock Plotter PA - Week 5.
###              Then it defines two functions for either vertical plots or
###              horizontal plots, each function contains while loops, if-elif-else to check
###              the plot string and print the correct plot with the asterisks in the desired
###              location. Then, there is the main() definition, which asks the user for the input
###              for both plot_mode and plot_string, if the user inputs an invalid string, while loops
###              are used to ask for the inputs repeatedly until the user inputs a valid string. The
###              main() function also uses uses if-elif to check if plot mode is vertical or horizontal
###              and then calls the appropriate function. The program runs by calling the main() function.
###

def vertical_plot(plot_string):
    '''
    This function is used if plot mode is vertical, it has a while loop
    with a nested if-elif to print the plot correctly. This function has plot_string
    as a parameter.
    plot_string: User input string that specifies where asterisks should be/how the
                 graph should look like.
    '''

    # Index for the while loop.
    vertical_i = 0
    # Stores current number, used to print the correct spacing so the asterisk will be in the
    # correct position.
    position = 0
    # Stores current character ("u" or "d").
    character = ""
    # Stores half of the plot width.
    plot_center = 8
    print(19 * "#")
    # This while loop runs for every two characters in 'plot_string', storing the current character
    # in the 'character' variable and using if-elif to check if it is a "u" or "d" and performing
    # string multiplication accordingly.
    while vertical_i < len(plot_string):
        character = plot_string[vertical_i]
        if character == "u":
            position += int(plot_string[vertical_i + 1])
            print("#" + (plot_center + position) * " " + "*" + (plot_center - position) * " " + "#")
        elif character == "d":
            position -= int(plot_string[vertical_i + 1])
            print("#" + (plot_center + position) * " " + "*" + (plot_center - position) * " " + "#")
        vertical_i += 2
    print(19 * "#")

def horizontal_plot(plot_string):
    '''
    This function is used if plot mode is horizontal. It has a while loop and a nested while
    loop inside it. In the nestes while loop there are if-elif and if-else statements to
    count correct number of spaces and asterisks to be printed in each row. This function has
    plot string as a parameter.
    plot_string: User input string that specifies where asterisks should be/how the
                 graph should look like.
    '''

    # Index for the outer while loop.
    outer_i = 0
    # Stores current character ("u" or "d").
    character = ""
    print((len(plot_string) // 2 + 4) * "#")
    # This outer loop is responsible for printing the edges of the plot. It iterates
    # 17 times (height of plot).
    while outer_i < 17:
        # Stores current level.
        current_level = 8
        # Index for the inner (nested) while loop.
        inner_i = 0
        print("# ", end="")
        # This while loop runs for every two characters in 'plot_string', storing the current
        # character in the 'character' variable and using if-elif to check if it is a "u" or
        # "d" to update 'current_level' accordingly. Inside the if-elif there is an if-else
        # to check if it should print either a space or an asterisk depending on the level
        # and height.
        while inner_i < len(plot_string):
            if plot_string[inner_i] == "u":
                current_level += int(plot_string[inner_i + 1])
                if current_level == 16 - outer_i:
                    print("*", end="")
                else:
                    print(" ", end="")
            elif plot_string[inner_i] == "d":
                current_level -= int(plot_string[inner_i + 1])
                if current_level == 16 - outer_i:
                    print("*", end="")
                else:
                    print(" ", end="")
            inner_i += 2
        print(" #")
        outer_i += 1
    print((len(plot_string) // 2 + 4) * "#")

def main():
    plot_mode = input("Enter stock plotter mode:\n")

    # Checks if 'plot_mode' is either vertical or horizontal, if it is neither it asks the user
    # input again until the condition is true.
    while not (plot_mode == "vertical" or plot_mode == "horizontal"):
        plot_mode = input("Enter stock plotter mode:\n")

    plot_string = input("Enter stock plot input string:\n")

    # Checks if 'plot_string' is even, if it is not, it asks the user input again until the
    # condition is true.
    while len(plot_string) % 2 != 0:
        plot_string = input("Enter stock plot input string:\n")

    # Checks if plot mode is vertical or horizontal and calls the according function.
    if plot_mode == "vertical":
        vertical_plot(plot_string)
    elif plot_mode == "horizontal":
        horizontal_plot(plot_string)

main()