//******************************************************************************
//Canvas�̊e���\�b�h�������v���O����
//******************************************************************************


//==============================================================================
//�N���X���C�u�����̃C���|�[�g
//==============================================================================
import java.awt.*;
import javax.swing.*;


//==============================================================================
//���C���N���X
//==============================================================================
public class Canvas_test
{

 //==============================================================================
 //���C�����\�b�h
 //==============================================================================
 public static void main(String[] args)
 {

  //============================================================================
  //�t���[���̍쐬
  JFrame frame = new JFrame();
 
  //�^�C�g����ݒ�
  frame.setTitle("Canvas_test");

  //�t���[���i�E�B���h�E�j�̃T�C�Y��ݒ�
  frame.setBounds(100, 100, 600, 400);

  //�~�{�^�����������Ƃ��̏������L�q
  frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

  //�E�B���h�E�T�C�Y�͌Œ�
  frame.setResizable(true);

  //���C�A�E�g�͎蓮
  frame.setLayout(null);


  //============================================================================  
  //�R���e���g�y�C���̍쐬
  JPanel cp = new JPanel();

  //���C�A�E�g�͎蓮
  cp.setLayout(null);

  //�t���[���ɃR���e���g�y�C����o�^
  frame.add(cp);

  //�R���e���g�y�C���̓\��t���ʒu�E�傫����ݒ�
  cp.setBounds (0, 0, 100, 100);
 

  //============================================================================   
  //�L�����o�X�̍쐬
  TestCanvas canvas = new TestCanvas();

  //�L�����o�X���R���e���g�E�y�C���ɓo�^
  cp.add(canvas);

  //�L�����p�X�̈ʒu�̓R���e���g�y�C���ɍ��킹��B
  //�L�����o�X�̃T�C�Y�̓R���e���g�y�C���Ɠ����ɂ���B
  canvas.setBounds (10, 10, 500, 300);

  


  //============================================================================   
  //�Ō�ɁA�t���[���̉���
  frame.setVisible(true);
 }

}

