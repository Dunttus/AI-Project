# Draw matplotlib charts and save them to the model directory
import matplotlib.pyplot as plt
import Lokari_apache_AD.config as config


def draw_anomaly_check(data):

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
    plt.clf()

    return


def draw_training_history(model):

    plt.plot(linewidth=0.5)
    plt.plot(model.history['loss'], label='loss')
    plt.plot(model.history['status_loss'], label='Status')
    plt.plot(model.history['byte_loss'], label='Byte')
    plt.plot(model.history['rtime_loss'], label='Request time')
    plt.plot(model.history['method_loss'], label='Method')
    plt.plot(model.history['url_loss'], label='Url')
    plt.yscale('log')
    plt.legend()
    plt.ylabel('Loss')
    plt.xlabel('Epoch')

    plot_file = 'saved_models/' + config.VERSION + \
                '/training_history_plot-' + config.VERSION + '.png'
    plt.savefig(plot_file)
    plt.clf()

    return
