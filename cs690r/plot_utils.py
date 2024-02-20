import matplotlib.pyplot as plt
from matplotlib import animation


def plot_time_series(time_series, series_type, title=None):
    '''
    Parameters
    ----------
    time_series : array with shape (N, 3)
        The time_series you need to visualize.
    
    series_type: str
        The type of the time series. Options are 'pos', 'vel', and 'acc'.

    title: str, optional
        The title of the plot.
    '''
    if time_series.shape[1] != 3:
        raise ValueError('The shape of time_series should be (N, 3).')
    
    if series_type not in ['pos', 'vel', 'acc']:
        raise ValueError('series_type should be chosen from ["pos", "vel", "acc"].')
        
    row_sz = 3
    col_sz = 7
    fig, ax = plt.subplots(figsize=(col_sz, row_sz))
    ax.plot(time_series)
    ax.set_xlabel('Frame')
    
    ylabel_mapping = {'pos': 'Pos ($m$)', 'vel': 'Vel ($m/s$)', 'acc': 'Acc ($m/s^2$)'}
    ax.set_ylabel(ylabel_mapping[series_type])
    
    ax.set_title(title)
    ax.legend(['X-axis', 'Y-axis', 'Z-axis'])
    fig.tight_layout()
    plt.show()
    
    
def animate_trajectory(trajectory, title=None):
    '''
    Parameters
    ----------
    trajectory : array with shape (N, 3)
        The trajectory you need to visualize.

    title : str, optional
        The title of the plot.
        
        
    Return type
    ----------
    ani : animation
    '''
    
    if trajectory.shape[1] != 3:
        raise ValueError('The shape of trajectory should be (N, 3).')

    N = trajectory.shape[0]
    
    trajectory -= trajectory[0]
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(*trajectory[0])
    
    xmin, xmax = min(trajectory[:, 0]), max(trajectory[:, 0])
    ymin, ymax = min(trajectory[:, 1]), max(trajectory[:, 1])
    zmin, zmax = min(trajectory[:, 2]), max(trajectory[:, 2])
    
    def update(num):
        ax.clear()
        ax.plot(*trajectory[:num * 10].T)
        
        ax.set_xlim([xmin, xmax])
        ax.set_ylim([ymin, ymax])
        ax.set_zlim([zmin, zmax])
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        ax.set_title(title)
    
    ax.set_xlim([xmin, xmax])
    ax.set_ylim([ymin, ymax])
    ax.set_zlim([zmin, zmax])
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title(title)
    
    ani = animation.FuncAnimation(fig, update, N // 10, interval=1, blit=False)
    return ani


def compare_trajectory(data1, data2, title1, title2):
    '''
    Parameters
    ----------
    data1 : sensor/mocap data object
        This object must contain acc, vel, and pos
    
    data2 : sensor/mocap data object
        This object must contain acc, vel, and pos
        
    title1 : str
        The plot title for data1
        Sepecify what sensor it is

    title2 : str
        The plot title for data2
        Sepecify what sensor it is
    '''
    
    n_rows = 3
    n_cols = 2
    row_sz = 2
    col_sz = 4.5
    fig = plt.figure(figsize=(n_cols * col_sz, n_rows * row_sz))
    ax = fig.add_subplot(n_rows, n_cols, 1)
    ax.plot(data1.acc)
    ax.set_xlabel('Frame')
    ax.set_ylabel('Acc ($m/s^2$)')
    ax.set_title(title1)
    ax.legend(['X-axis', 'Y-axis', 'Z-axis'], ncol=3, fontsize='small')

    ax = fig.add_subplot(n_rows, n_cols, 2)
    ax.plot(data2.acc)
    ax.set_xlabel('Frame')
    ax.set_ylabel('Acc ($m/s^2$)')
    ax.set_title(title2)
    ax.legend(['X-axis', 'Y-axis', 'Z-axis'], ncol=3, fontsize='small')

    ax = fig.add_subplot(n_rows, n_cols, 3)
    ax.plot(data1.vel)
    ax.set_xlabel('Frame')
    ax.set_ylabel('Vel ($m/s$)')
    ax.set_title(title1)
    ax.legend(['X-axis', 'Y-axis', 'Z-axis'], ncol=3, fontsize='small')

    ax = fig.add_subplot(n_rows, n_cols, 4)
    ax.plot(data2.vel)
    ax.set_xlabel('Frame')
    ax.set_ylabel('Vel ($m/s$)')
    ax.set_title(title2)
    ax.legend(['X-axis', 'Y-axis', 'Z-axis'], ncol=3, fontsize='small')

    ax = fig.add_subplot(n_rows, n_cols, 5)
    ax.plot(data1.pos - data1.pos[0])
    ax.set_xlabel('Frame')
    ax.set_ylabel('Pos ($m$)')
    ax.set_title(title1)
    ax.legend(['X-axis', 'Y-axis', 'Z-axis'], ncol=3, fontsize='small')

    ax = fig.add_subplot(n_rows, n_cols, 6)
    ax.plot(data2.pos - data2.pos[0])
    ax.set_xlabel('Frame')
    ax.set_ylabel('Pos ($m/s^2$)')
    ax.set_title(title2)
    ax.legend(['X-axis', 'Y-axis', 'Z-axis'], ncol=3, fontsize='small')
    fig.tight_layout()
    plt.show()