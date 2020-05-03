# Draw matplotlib charts and save them to the model directory
import matplotlib.pyplot as plt
import Lokari_apache_AD.config as config


def make_plot(data):

    # TODO: separate plot drawing stuff, now this messes up the training plot
    # Validation graphics
    plt.plot(data)
    plt.grid(True)
    # plt.yscale('symlog', linthreshy=0.1)
    # plt.ylim(-1,10)
    plt.ylabel('Root-mean-square deviation difference')
    plt.xlabel('Log line number')
    plt.legend(['url', 'byte', 'rtime', 'method', 'status'])
    plot_file = 'saved_models/' + config.VERSION + \
                '/training_data_analysis-' + config.VERSION + '.png'
    plt.savefig(plot_file)

