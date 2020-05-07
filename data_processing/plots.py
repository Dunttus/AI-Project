# Draw matplotlib charts and save them to the model directory
import matplotlib.pyplot as plt
import config as config


def draw_anomaly_check(data):

    # Validation graphics
    plt.plot(data, linewidth=config.LINE_WIDTH)
    plt.grid(True)
    # plt.ylim(-1,10)
    plt.ylabel('Root-mean-square deviation difference')
    plt.xlabel('Log line number')
    plt.legend(['url', 'byte', 'rtime', 'method', 'status'])

    plot_file = 'saved_models/' + config.VERSION + \
                '/training_data_analysis-' + config.VERSION + '.png'
    plt.savefig(plot_file, dpi=600)
    plt.clf()

    return


def draw_anomaly_check_log(data):

    # Validation graphics, logarithmic scale
    plt.plot(data, linewidth=config.LINE_WIDTH)
    plt.grid(True)
    plt.yscale('symlog', linthreshy=0.1)
    # plt.ylim(-1,10)
    plt.ylabel('Root-mean-square deviation difference')
    plt.xlabel('Log line number')
    plt.legend(['url', 'byte', 'rtime', 'method', 'status'])

    plot_file = 'saved_models/' + config.VERSION + \
                '/training_data_analysis_log-' + config.VERSION + '.png'
    plt.savefig(plot_file, dpi=600)
    plt.clf()

    return


def draw_training_history(model):

    plt.plot(model.history['loss'], label='loss',
             linewidth=config.LINE_WIDTH)
    plt.plot(model.history['status_loss'], label='Status',
             linewidth=config.LINE_WIDTH)
    plt.plot(model.history['byte_loss'], label='Byte',
             linewidth=config.LINE_WIDTH)
    plt.plot(model.history['rtime_loss'], label='Request time',
             linewidth=config.LINE_WIDTH)
    plt.plot(model.history['method_loss'], label='Method',
             linewidth=config.LINE_WIDTH)
    plt.plot(model.history['url_loss'], label='Url',
             linewidth=config.LINE_WIDTH)
    plt.yscale('log')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend()
    plt.grid(True)

    plot_file = 'saved_models/' + config.VERSION + \
                '/training_history_plot-' + config.VERSION + '.png'
    plt.savefig(plot_file, dpi=600)
    plt.clf()

    return
