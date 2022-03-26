import wx
from wx import glcanvas
from OpenGL.GL import *
from OpenGL.GLUT import *
#---------------------------------------------------
class CanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent, -1)
        self.context = glcanvas.GLContext(self)
        self.init = False
        # Cube 3D start rotation
        self.last_X = self.x = 30
        self.last_Y = self.y = 30
        self.Bind(wx.EVT_SIZE, self.sizeCallback)
        self.Bind(wx.EVT_PAINT, self.paintCallback)
        self.Bind(wx.EVT_LEFT_DOWN, self.mouseDownCallback)
        self.Bind(wx.EVT_LEFT_UP, self.mouseUpCallback)
        self.Bind(wx.EVT_MOTION, self.mouseMotionCallback)
    def sizeCallback(self, event):
        wx.CallAfter(self.setViewport)
        event.Skip()
    def setViewport(self):
        self.size = self.GetClientSize()
        self.SetCurrent(self.context)
        glViewport(0, 0, self.size.width, self.size.height)
    def paintCallback(self, event):
        wx.PaintDC(self)
        self.SetCurrent(self.context)
        if not self.init:
            self.initGL()
            self.init = True
        self.onDraw()
    def mouseDownCallback(self, event):
        self.CaptureMouse()
        self.x, self.y = self.last_X, self.last_Y = event.GetPosition()
    def mouseUpCallback(self, evt):
        self.ReleaseMouse()
    def mouseMotionCallback(self, evt):
        if evt.Dragging() and evt.LeftIsDown():
            self.last_X, self.last_Y = self.x, self.y
            self.x, self.y = evt.GetPosition()
            self.Refresh(False)
#-----------------------------------------------------
class CubeCanvas(CanvasBase):
    def initGL(self):
        # set viewing projection
        glMatrixMode(GL_PROJECTION)
        glFrustum(-0.5, 0.5, -0.5, 0.5, 1.0, 3.0)
        # position viewer
        glMatrixMode(GL_MODELVIEW)
        glTranslatef(0.0, 0.0, -2.0)
        # position object
        glRotatef(self.y, 1.0, 0.0, 0.0)
        glRotatef(self.x, 0.0, 1.0, 0.0)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
    def onDraw(self):
        # clear color and depth buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # draw six faces of a cube
        glBegin(GL_QUADS)
        glNormal3f( 0.0, 0.0, 1.0)
        glVertex3f( 0.5, 0.5, 0.5)
        glVertex3f(-0.5, 0.5, 0.5)
        glVertex3f(-0.5,-0.5, 0.5)
        glVertex3f( 0.5,-0.5, 0.5)
        glNormal3f( 0.0, 0.0,-1.0)
        sglVertex3f(-0.5,-0.5,-0.5)
#===========================================================
app = wx.App()
frame = wx.Frame(None, size=(300,230))
#GUI(frame)
frame.Show()
app.MainLoop()

