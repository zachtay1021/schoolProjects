# Zachary Taylor - CINF405 Advanced Concepts and Practices in Software Development

import cpu
import gpu
import ram
import all


def main():
    exitFalse = True
    while exitFalse:
        userInput = int(input('''
                Please select an option below:
                1) CPU Data
                2) GPU DATA
                3) RAM Data
                4) All Data
                5) Exit
                '''))

        if userInput == 1:
            cpuExitTrue = False
            choice_cpu = cpu.CPU()

            while cpuExitTrue is False:
                cpu_selection = int(input('''
                Please select an option below:
                1) Year by year analysis
                2) Moore's Law (two year) analysis
                3) Exit
                '''))

                if cpu_selection == 1:
                    choice_cpu.avg_perc_inc()

                elif cpu_selection == 2:
                    choice_cpu.two_year_inc()

                elif cpu_selection == 3:
                    cpuExitTrue = True

                else:
                    print('Invalid Selection')

        elif userInput == 2:
            gpuExitTrue = False
            choice_gpu = gpu.GPU()

            while gpuExitTrue is False:
                gpu_selection = int(input('''
                Please select an option below:
                1) Year by year analysis
                2) Moore's Law (two year) analysis
                3) Exit
                '''))

                if gpu_selection == 1:
                    choice_gpu.avg_perc_inc()

                elif gpu_selection == 2:
                    choice_gpu.two_year_inc()

                elif gpu_selection == 3:
                    gpuExitTrue = True

                else:
                    print('Invalid Selection')

        elif userInput == 3:
            ramExitTrue = False
            choice_ram = ram.RAM()

            while ramExitTrue is False:
                ram_selection = int(input('''
                Please select an option below:
                1) Year by year analysis
                2) Moore's Law (two year) analysis
                3) Exit
                '''))

                if ram_selection == 1:
                    choice_ram.avg_perc_inc()

                elif ram_selection == 2:
                    choice_ram.two_year_inc()

                elif ram_selection == 3:
                    ramExitTrue = True

                else:
                    print('Invalid Selection')

        elif userInput == 4:
            allExitTrue = False
            choice_all = all.ALL()

            while allExitTrue is False:
                all_selection = int(input('''
                Please select an option below:
                1) Year by year analysis
                2) Moore's Law (two year) analysis
                3) Exit
                '''))

                if all_selection == 1:
                    choice_all.avg_perc_inc()

                elif all_selection == 2:
                    choice_all.two_year_inc()

                elif all_selection == 3:
                    allExitTrue = True

                else:
                    print('Invalid Selection')

        elif userInput == 5:
            exitFalse = False

        else:
            print('Invalid selection')


main()
