U
    �|�_�  �                   @   s   G d d� d�Z dS )c                   @   s4   e Zd Zdd� Zdd� Zdd� Zdd� Zd	d
� ZdS )�ATMCardc                 C   s"   || _ || _|| _|| _|| _d S �N)�card�custPin�
BalanceIDR�
BalanceUSD�
BalanceKWD)�selfr   r   r   r   r   � r	   �atm_card.py�__init__   s
    zATMCard.__init__c                 C   s   | j S r   )r   �r   r	   r	   r
   �pin	   s    zATMCard.pinc                 C   s   | j S r   )r   r   r	   r	   r
   �
balanceidr   s    zATMCard.balanceidrc                 C   s   | j S r   )r   r   r	   r	   r
   �
balanceusd   s    zATMCard.balanceusdc                 C   s   | j S r   )r   r   r	   r	   r
   �
balancekwd   s    zATMCard.balancekwdN)�__name__�
__module__�__qualname__r   r   r   r   r   r	   r	   r	   r
   r      s
   r   N)r   r	   r	   r	   r
   �<module>   �    