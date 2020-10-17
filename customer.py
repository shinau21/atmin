U
    H+�_K  �                   @   s(   d dl Z d dlmZ G dd� de�ZdS )�    N)�ATMCardc                       s�   e Zd Zd)� fdd�	Zdd� Zdd� Zd	d
� Zdd� Zdd� Zdd� Z	dd� Z
dd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd � Zd!d"� Zd#d$� Zd%d&� Zd'd(� Z�  ZS )*�Customerr   � c                    s  t � �|||||� || _t�dddd�}|�� }d| j }|�|� |�� }|D ]�}t|d �| _	|d | _
|d | _|d	 | _|d
 | _|d | _|d | _|d | _|d | _|d | _|d | _|d | _|d | _t|d �| _t|d �| _t|d �| _t|d �| _qRd S )N�	localhost�rootr   �atminz#SELECT * FROM nasabah WHERE id='%d'�   �   �   �   �   �   �   �   �	   �
   �   �   �   �   �   �   �   )�super�__init__�id�pymysql�connect�cursor�executeZfetchall�int�card�name�jk�desa�kec�kab�tml�tl�umur�ibu�jenis�nik�kk�custPin�
BalanceIDR�float�
BalanceUSD�
BalanceKWD)�selfr   r!   r.   r"   r#   r$   r%   r&   r'   r(   r)   r*   r+   r,   r-   r/   r1   r2   �dbr   �sql�results�row��	__class__� �customer.pyr      s2    













zCustomer.__init__c                 C   s   | j S �N)r"   �r3   r:   r:   r;   �	checkName!   s    zCustomer.checkNamec                 C   s   | j S r<   )r#   r=   r:   r:   r;   �checkGender$   s    zCustomer.checkGenderc                 C   s   | j d | j d | j S )N� )r$   r%   r&   r=   r:   r:   r;   �checkAlamat'   s    zCustomer.checkAlamatc                 C   s   | j S r<   )r)   r=   r:   r:   r;   �	checkUmur*   s    zCustomer.checkUmurc                 C   s   | j S r<   )r+   r=   r:   r:   r;   �
checkJenis-   s    zCustomer.checkJenisc                 C   s   | j S r<   )r!   r=   r:   r:   r;   �	checkCard0   s    zCustomer.checkCardc                 C   s   | j S r<   )r.   r=   r:   r:   r;   �checkPin3   s    zCustomer.checkPinc                 C   s<   t �dddd�}|�� }d|| jf }|�|� |��  d S )Nr   r   r   r   z)UPDATE nasabah SET pin='%d' WHERE id='%d')r   r   r   r   r   �commit)r3   �newr4   r   r5   r:   r:   r;   �	changePin6   s
    
zCustomer.changePinc                 C   s   | j S r<   )r*   r=   r:   r:   r;   �checkIbu=   s    zCustomer.checkIbuc                 C   s   | j S r<   )r/   r=   r:   r:   r;   �checkIDR@   s    zCustomer.checkIDRc                 C   s   | j S r<   )r1   r=   r:   r:   r;   �checkUSDC   s    zCustomer.checkUSDc                 C   s   | j S r<   )r2   r=   r:   r:   r;   �checkKWDF   s    zCustomer.checkKWDc                 C   sL   |  j |8  _ t�dddd�}|�� }d| j | jf }|�|� |��  d S )Nr   r   �123456r   z/UPDATE nasabah SET saldo_idr='%d' WHERE id='%d'�r/   r   r   r   r   r   rF   �r3   Znominalr4   r   r5   r:   r:   r;   �
witdrawIDRI   s    
zCustomer.witdrawIDRc                 C   sL   |  j |8  _ t�dddd�}|�� }d| j | jf }|�|� |��  d S )Nr   r   rM   r   z/UPDATE nasabah SET saldo_usd='%d' WHERE id='%d'�r1   r   r   r   r   r   rF   rO   r:   r:   r;   �
witdrawUSDQ   s    
zCustomer.witdrawUSDc                 C   sL   |  j |8  _ t�dddd�}|�� }d| j | jf }|�|� |��  d S �Nr   r   rM   r   z/UPDATE nasabah SET saldo_kwd='%d' WHERE id='%d'�r2   r   r   r   r   r   rF   rO   r:   r:   r;   �
witdrawKWDY   s    
zCustomer.witdrawKWDc                 C   sL   |  j |7  _ t�dddd�}|�� }d| j | jf }|�|� |��  d S rS   rN   rO   r:   r:   r;   �
depositIDRa   s    
zCustomer.depositIDRc                 C   sL   |  j |7  _ t�dddd�}|�� }d| j | jf }|�|� |��  d S rS   rQ   rO   r:   r:   r;   �
depositUSDi   s    
zCustomer.depositUSDc                 C   sL   |  j |7  _ t�dddd�}|�� }d| j | jf }|�|� |��  d S rS   rT   rO   r:   r:   r;   �
depositKWDq   s    
zCustomer.depositKWD)r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   )�__name__�
__module__�__qualname__r   r>   r?   rA   rB   rC   rD   rE   rH   rI   rJ   rK   rL   rP   rR   rU   rV   rW   rX   �__classcell__r:   r:   r8   r;   r      s&   r   )r   Zatm_cardr   r   r:   r:   r:   r;   �<module>   s   