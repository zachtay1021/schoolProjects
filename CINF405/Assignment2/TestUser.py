# Zach Taylor - CINF405 Advanced Concepts and Practices in Software Development

import Country
import State


def main():
    exitFalse = True
    while exitFalse:  # Continues to run until exitFalse is set to False
        print('''
                This program displays average tuition cost data for US States for recent years.
                Data is displayed for a specific state or the entire Country.

                1) Entire United States
                2) Specific State
                3) Exit
                ''')
        userInput = int(input('Please select one of the above options: '))

        if userInput == 1:
            country = Country.Country()
            country.country_avg_tuition()

            print('The overall average tuition cost for the years covered is: ${}'.format(country.country_avg_tuition()))
            print('The average rise between years for all the years covered is: {}%'.format(country.country_avg_rise()))
            print('The predicted tuition for the next year based on the rise for last year is: ${}'.format(country.country_pred_one_year()[0]))
            print('The predicted tuition for the next year based on the average tuition rise for all years is: ${}'.format(country.country_pred_one_year()[1]))
            print('The predicted tuition rise two years out based on the tuition rise for the last year is: {}%'.format(country.country_pred_two_year()[0]))
            print('The predicted tuition rise two years out based on the average tuition rise for the last two years is: {}%'.format(country.country_pred_two_year()[1]))
            print('The predicted tuition rise two years out based on the average tuition rise for all the years is: {}%'.format(country.country_pred_two_year()[2]))

        elif userInput == 2:
            userState = input('Please enter a state: ')
            state = State.State(userState)

            print('The overall average tuition cost for the years covered is: ${}'.format(state.avg_tuition()))
            print('The average rise between years for all the years covered is: {}%'.format(state.avg_rise()))
            print('The predicted tuition for the next year based on the rise for last year is: ${}'.format(state.pred_one_year()[0]))
            print('The predicted tuition for the next year based on the average tuition rise for all years is: ${}'.format(state.pred_one_year()[1]))
            print('The predicted tuition rise two years out based on the tuition rise for the last year is: {}%'.format(state.pred_two_year()[0]))
            print('The predicted tuition rise two years out based on the average tuition rise for the last two years is: {}%'.format(state.pred_two_year()[1]))
            print('The predicted tuition rise two years out based on the average tuition rise for all the years is: {}%'.format(state.pred_two_year()[2]))

        elif userInput == 3:
            print('Exiting')
            exitFalse = False  # Closes the main while loop
        else:
            print('Invalid input')  # If the user inputs something other than one of the above options, print an error


if __name__ == '__main__':
    main()
