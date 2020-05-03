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
    plt.savefig(plot_file, dpi=300)
    plt.clf()

    return


def draw_training_history(model):

    plt.plot(model.history['loss'], label='loss', linewidth=0.5)
    plt.plot(model.history['status_loss'], label='Status', linewidth=0.5)
    plt.plot(model.history['byte_loss'], label='Byte', linewidth=0.5)
    plt.plot(model.history['rtime_loss'], label='Request time', linewidth=0.5)
    plt.plot(model.history['method_loss'], label='Method', linewidth=0.5)
    plt.plot(model.history['url_loss'], label='Url', linewidth=0.5)
    plt.yscale('log')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend()
    plt.grid(True)

    plot_file = 'saved_models/' + config.VERSION + \
                '/training_history_plot-' + config.VERSION + '.png'
    plt.savefig(plot_file, dpi=300)
    plt.clf()

    return
